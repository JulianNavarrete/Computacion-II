#!/usr/bin/python3

import asyncio
import subprocess


async def function(r, w):
    addr = w.get_extra_info('peername')
    print("Tengo una conexión de", str(addr))
    msg = await (r.read(20)).decode('utf-8')
    if msg != "exit":
        res = subprocess.Popen([msg], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        std_out, std_err = res.communicate()
        if std_out != "":
            msg = "\nOK\n" + std_out
        if std_err != "":
            msg = "\nERROR\n" + std_err

        w.write(msg.encode('utf-8'))
        await w.drain()
    else:
        w.close()
        print("Conexión cerrada", addr)


async def main():
    host = "localhost"
    port = 8000
    print("Esperando conexiones...")
    s = await asyncio.start_server(function, host, port)
    async with s:
        await s.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
