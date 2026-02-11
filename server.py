from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

IP = "192.168.1.5"
PORT = 4443

httpd = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=f"{IP}.pem", keyfile=f"{IP}-key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"HTTPS rodando em: https://{IP}:{PORT}/hub.html")
httpd.serve_forever()
