"""Exemplo prático: síncrono vs assíncrono em Python.

Executa três versões da mesma ideia:
1) Síncrona: bloqueia em cada operação.
2) Assíncrona sequencial: usa await, mas ainda espera uma por vez.
3) Assíncrona concorrente: agenda várias tarefas ao mesmo tempo.
4) Paralelismo com threads: executa tarefas de I/O em paralelo usando threads.
"""

from __future__ import annotations

import asyncio
import threading
import time


def tarefa_sincrona(nome: str, atraso: float) -> str:
    """Simula uma operação de I/O usando sleep bloqueante."""
    print(f"[sync] Iniciando {nome} ({atraso:.1f}s)")
    time.sleep(atraso)
    print(f"[sync] Finalizando {nome}")
    return f"{nome} concluída"


async def tarefa_assincrona(nome: str, atraso: float) -> str:
    """Simula uma operação de I/O usando asyncio.sleep (não bloqueante)."""
    print(f"[async] Iniciando {nome} ({atraso:.1f}s)")
    await asyncio.sleep(atraso)
    print(f"[async] Finalizando {nome}")
    return f"{nome} concluída"


def executar_sincrono() -> list[str]:
    """Executa tudo de forma bloqueante, uma tarefa por vez."""
    inicio = time.perf_counter()
    resultados = [
        tarefa_sincrona("download_1", 1.5),
        tarefa_sincrona("download_2", 1.0),
        tarefa_sincrona("download_3", 2.0),
    ]
    fim = time.perf_counter()
    print(f"Tempo total (síncrono): {fim - inicio:.2f}s\n")
    return resultados


async def executar_assincrono_sequencial() -> list[str]:
    """Usa async/await, mas ainda de forma sequencial."""
    inicio = time.perf_counter()
    resultados = [
        await tarefa_assincrona("download_1", 1.5),
        await tarefa_assincrona("download_2", 1.0),
        await tarefa_assincrona("download_3", 2.0),
    ]
    fim = time.perf_counter()
    print(f"Tempo total (assíncrono sequencial): {fim - inicio:.2f}s\n")
    return resultados


async def executar_assincrono_concorrente() -> list[str]:
    """Agenda as tarefas juntas para aproveitar o event loop."""
    inicio = time.perf_counter()
    resultados = await asyncio.gather(
        tarefa_assincrona("download_1", 1.5),
        tarefa_assincrona("download_2", 1.0),
        tarefa_assincrona("download_3", 2.0),
    )
    fim = time.perf_counter()
    print(f"Tempo total (assíncrono concorrente): {fim - inicio:.2f}s\n")
    return resultados


def executar_threading() -> list[str]:
    """Executa tarefas de I/O em paralelo usando threads."""
    resultados = ["", "", ""]
    tarefas = [
        ("download_1", 1.5),
        ("download_2", 1.0),
        ("download_3", 2.0),
    ]

    def worker(indice: int, nome: str, atraso: float) -> None:
        print(f"[thread] Iniciando {nome} ({atraso:.1f}s)")
        time.sleep(atraso)
        resultados[indice] = f"{nome} concluída"
        print(f"[thread] Finalizando {nome}")

    inicio = time.perf_counter()
    threads = [
        threading.Thread(target=worker, args=(indice, nome, atraso))
        for indice, (nome, atraso) in enumerate(tarefas)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    fim = time.perf_counter()
    print(f"Tempo total (threading): {fim - inicio:.2f}s\n")
    return resultados


async def main() -> None:
    print("=== 1) Versão síncrona ===")
    resultados_sync = executar_sincrono()
    print("Resultados:", resultados_sync)

    print("=== 2) Versão assíncrona sequencial ===")
    resultados_async_seq = await executar_assincrono_sequencial()
    print("Resultados:", resultados_async_seq)

    print("=== 3) Versão assíncrona concorrente ===")
    resultados_async_conc = await executar_assincrono_concorrente()
    print("Resultados:", resultados_async_conc)

    print("=== 4) Versão com threading ===")
    resultados_threading = executar_threading()
    print("Resultados:", resultados_threading)


if __name__ == "__main__":
    asyncio.run(main())
