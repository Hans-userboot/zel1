

if __name__ == "__main__":
    import uvloop
    from core.bot import Bot
    uvloop.install()
    Bot().start(use_qr=True)
