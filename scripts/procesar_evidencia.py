import os
import re

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extraer_ip_whatweb():
    # Mantenemos tu ruta personalizada para la IP
    path = os.path.join(BASE_DIR, "evidencia", "whatweb_tech_fingerprint", "tech.txt")
    if os.path.exists(path):
        with open(path, 'r') as f:
            contenido = f.read()
            ip = re.search(r'IP\[(.*?)\]', contenido)
            return ip.group(1) if ip else "104.16.x.x"
    return "104.16.x.x"

def procesar_filtrados():
    print("🎯 Procesando subdominios desde la lista filtrada...")
    ip_base = extraer_ip_whatweb()
    
    # Rutas de entrada (Filtrados) y salida (CSV)
    archivo_csv = os.path.join(BASE_DIR, "reportes", "analisis_maestro_cloudflare.csv")
    sub_path = os.path.join(BASE_DIR, "evidencia", "Sublist3r", "clean_subdomains.txt")

    if not os.path.exists(sub_path):
        print(f"❌ No encontré el archivo: {sub_path}")
        return

    with open(sub_path, 'r') as entrada, open(archivo_csv, 'w') as salida:
        # Cabecera del CSV
        salida.write("Subdominio,IP,Tecnologia,Fuente\n")
        
        count = 0
        for linea in entrada:
            url = linea.strip()
            if not url: continue
            
            # Limpieza básica por si quedó algún espacio o caracter raro
            url_limpia = url.split()[0] 
            
            # Escribimos la fila en el CSV
            salida.write(f"{url_limpia},{ip_base},Cloudflare,Sublist3r-Filtered\n")
            count += 1
                
    print(f"✅ ¡Éxito! Se generó el reporte con {count} activos únicos.")

if __name__ == "__main__":
    procesar_filtrados()
