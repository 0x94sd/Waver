import httpx
import pkgutil
import importlib
import holehe.modules

async def scanner_email(email):
    client = httpx.AsyncClient()
    resultats = []

    for importer, module_name, _ in pkgutil.walk_packages(
        path=holehe.modules.__path__,
        prefix="holehe.modules.",
        onerror=lambda x: None
    ):
        try:
            module = importlib.import_module(module_name)
            func_name = module_name.split(".")[-1]
            if hasattr(module, func_name):
                func = getattr(module, func_name)
                await func(email, client, resultats)
        except Exception:
            pass

    await client.aclose()
    return [r for r in resultats if r.get("exists")]