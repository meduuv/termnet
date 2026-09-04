from dataclasses import dataclass
import socket

@dataclass(frozen=True)
class Endpoint:
    host:str
    port:int

def resolve(host:str)->list[str]:
    if not host.strip(): raise ValueError("host is required")
    return sorted({item[4][0] for item in socket.getaddrinfo(host,None)})

def endpoint(host:str,port:int)->Endpoint:
    if not 1<=port<=65535: raise ValueError("port out of range")
    return Endpoint(host,port)
