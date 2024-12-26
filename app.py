from flask import Flask, jsonify, render_template
import serial

# Создаем экземпляр Flask приложения
app = Flask(__name__)

# Настраиваем последовательный порт (замените 'COM5' на нужный вам порт)
ser = serial.Serial('COM5',9600)
# Переменные для хранения данных
data = {
    "temperature": None,  # Переменная для хранения температуры
    "humidity": None,     # Переменная для хранения влажности
    "pressure": None      # Переменная для хранения давления
}



@app.route("/")
def index():
    return render_template("index.html")

def read_serial_data():
    
    line = ser.readline().decode('utf-8')  # Читаем строку с последовательного порта
        
    try:
        # Ожидаем строку в формате: T:<temperature>, H:<humidity>, P:<pressure>
        t, p, h = line.split(' ')  # Разделяем строку на части
        data['temperature'] = float(t)  # Получаем значение температуры
        data['humidity'] = float(h)     # Получаем значение влажности
        data['pressure'] = float(p)     # Получаем значение давления
    except ValueError:
        print("Ошибка при разборе данных с последовательного порта")
    

@app.route('/data', methods=['POST'])
def receive_data():
      # Считываем данные с последовательного порта
    return jsonify(success=True)  # Возвращаем ответ об успешном получении данных

@app.route('/data', methods=['GET'])
def get_data():
    read_serial_data()  # Обновляем данные перед их возвращением
    return jsonify(data)  # Возвращаем данные в формате JSON



if __name__ == '__main__':
    
    app.run(host = '0.0.0.0', port = 5000)
