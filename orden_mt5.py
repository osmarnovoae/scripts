import sys
import MetaTrader5 as mt5

# Verifica argumentos
if len(sys.argv) < 4:
    print("Faltan argumentos: BUY|SELL SYMBOL VOLUME")
    sys.exit()

accion = sys.argv[1].upper()
symbol = sys.argv[2]
volume = float(sys.argv[3])

# Inicializa MT5
if not mt5.initialize():
    print("Error al iniciar MT5:", mt5.last_error())
    sys.exit()

# Obtiene precio actual
price = mt5.symbol_info_tick(symbol).ask if accion == "BUY" else mt5.symbol_info_tick(symbol).bid

# Prepara orden
order = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": volume,
    "type": mt5.ORDER_TYPE_BUY if accion == "BUY" else mt5.ORDER_TYPE_SELL,
    "price": price,
    "deviation": 10,
    "magic": 123456,
    "comment": "Orden desde C#",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

# Envía orden
result = mt5.order_send(order)

# Resultado
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("Error:", result.retcode)
else:
    print("Orden ejecutada correctamente")

# Cierra conexión
mt5.shutdown()