from flask import Flask, render_template, request, send_file
import descargador
import io

app = Flask('app')


@app.route('/')
def hello_world():
	return render_template("formulario.html")


@app.route("/procesar", methods=['POST'])
def procesar():
	url = request.form.get("url")
	paginas = request.form.get("paginas")
	nombre_sugerido = request.form.get("nombre")
	archivo_pdf_para_enviar_al_cliente = io.BytesIO()
	imagenes_en_pdf_como_bytes = descargador.descargar_libro(url, int(paginas))
	archivo_pdf_para_enviar_al_cliente.write(imagenes_en_pdf_como_bytes)
	archivo_pdf_para_enviar_al_cliente.seek(0)
	return send_file(archivo_pdf_para_enviar_al_cliente, mimetype="application/pdf",
					 download_name=nombre_sugerido + ".pdf",
					 as_attachment=True)


app.run(host='0.0.0.0', port=8080)

