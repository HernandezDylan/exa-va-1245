
import cv2
from pathlib import Path

# Carpeta principal del proyecto
carpeta_proyecto = Path(__file__).resolve().parent.parent

# Ruta de la imagen original
ruta_original = (
    carpeta_proyecto
    / "img-original-1245"
    / "img-hyundai-1245.jpg"
)

# Carpeta de resultados
carpeta_resultados = carpeta_proyecto / "resultados-img-1245"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

print("Buscando imagen en:", ruta_original)

# Leer imagen
img_hyundai_1344 = cv2.imread(str(ruta_original))

if img_hyundai_1344 is None:
    print("ERROR: No se encontró la imagen.")
    print("Verifica la carpeta y el nombre del archivo.")
    raise SystemExit

print("Imagen cargada correctamente.")


# Crear carpeta de resultados
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original
img_hyundai_0777 = cv2.imread(str(ruta_original))

if img_hyundai_0777 is None:
    raise FileNotFoundError(
        f"No se encontro la imagen: {ruta_original}"
    )

print("Imagen Hyundai cargada correctamente.")

# 3. Rotar 90 grados
img90_0777 = cv2.rotate(
    img_hyundai_0777,
    cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar 45 grados
alto, ancho = img_hyundai_0777.shape[:2]
centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0777 = cv2.warpAffine(
    img_hyundai_0777,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Cambiar tamaño a 600 x 500
img600x500_0777 = cv2.resize(
    img_hyundai_0777, (600, 500)
)


# Dibujar un rectangulo rojo mas grande
img_rojo_0777 = img_hyundai_0777.copy()

alto, ancho = img_rojo_0777.shape[:2]

cv2.rectangle(
    img_rojo_0777,
    (ancho // 4, alto // 4),
    (3 * ancho // 4, 3 * alto // 4),
    (0, 0, 255),
    5
)

cv2.imshow("Hyundai con rectangulo rojo", img_rojo_0777)
cv2.imwrite(
    str(carpeta_resultados / "img-hyundai4-1245.jpg"),
    img_rojo_0777
)


# Mostrar las imagenes una por una
cv2.imshow("1. Hyundai original", img_hyundai_0777)
print("Presiona una tecla para ver la siguiente imagen...")
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("2. Hyundai rotado 90 grados", img90_0777)
print("Presiona una tecla para ver la siguiente imagen...")
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("3. Hyundai rotado 45 grados", img45_0777)
print("Presiona una tecla para ver la siguiente imagen...")
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("4. Hyundai redimensionado", img600x500_0777)
print("Presiona una tecla para ver la siguiente imagen...")
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("5. Hyundai con rectangulo rojo", img_rojo_0777)
print("Presiona una tecla para terminar...")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Practica terminada correctamente.")
# 8. Guardar las imagenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-hyundai1-0777.jpg"),
    img90_0777
)

cv2.imwrite(
    str(carpeta_resultados / "img-hyundai2-0777.jpg"),
    img45_0777
)

cv2.imwrite(
    str(carpeta_resultados / "img-hyundai3-0777.jpg"),
    img600x500_0777
)

cv2.imwrite(
    str(carpeta_resultados / "img-hyundai4-0777.jpg"),
    img_rojo_0777
)

print("Imagenes procesadas y guardadas correctamente")

print("Hernadez Dylan NC 1245")