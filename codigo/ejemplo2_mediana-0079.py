import cv2

# Cargar la imagen
imagen = cv2.imread("tortuga.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original 0079", imagen)
cv2.imshow("Imagen con filtro de mediana 0079", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/tortuga_mediana 0079.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/tortuga_mediana 0079.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()