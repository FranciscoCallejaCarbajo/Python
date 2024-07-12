import qrcode

def main():
  # URL que deseas convertir a código QR
  url = "https://www.linkedin.com/in/<tu_user_aqui>/"

  # Crear objeto QR
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )

  # Agregar la URL al objeto QR
  qr.add_data(url)
  qr.make(fit=True)

  # Crear la imagen del QR
  img = qr.make_image(fill='black', back_color='white')

  # Guardar la imagen
  img.save("qr_code.png")

  print("Código QR generado y guardado como qr_code.png")

if __name__ == '__main__':
  main()
