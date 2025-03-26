import requests
import json

def obtener_info_ip(ip):
    # URL de la API de Shodan para obtener información de la IP
    url = f"https://internetdb.shodan.io/{ip}"

    # Realizar la solicitud GET para obtener los datos en formato JSON
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error al obtener datos para {ip}: {response.status_code}")
        return None

def mostrar_info_organizada(data):
    if data:
        print(f"Información de la IP: {data['ip']}\n")

        # Mostrar los puertos abiertos
        print("Puertos abiertos:")
        if 'ports' in data:
            print(", ".join(map(str, data['ports'])))
        else:
            print("No se encontraron puertos.")
        
        # Mostrar los CPEs
        print("\nCPEs asociados:")
        if 'cpes' in data:
            print("\n".join(data['cpes']))
        else:
            print("No se encontraron CPEs.")
        
        # Mostrar los hostnames
        print("\nHostnames:")
        if 'hostnames' in data:
            print("\n".join(data['hostnames']))
        else:
            print("No se encontraron hostnames.")
        
        # Mostrar las etiquetas
        print("\nEtiquetas (tags):")
        if 'tags' in data:
            print(", ".join(data['tags']))
        else:
            print("No se encontraron etiquetas.")
        
        # Mostrar las vulnerabilidades
        print("\nVulnerabilidades (vulns):")
        if 'vulns' in data:
            print("\n".join(data['vulns']))
        else:
            print("No se encontraron vulnerabilidades.")
        
    else:
        print("No se encontraron datos para la IP proporcionada.")

# Función principal
if __name__ == "__main__":
    # Pedir la IP al usuario
    ip = input("Introduce la IP que deseas consultar: ").strip()
    
    print(f"\nConsultando información para la IP: {ip}\n")
    
    # Obtener la información de la IP
    info = obtener_info_ip(ip)
    
    # Mostrar la información de manera organizada
    mostrar_info_organizada(info)
