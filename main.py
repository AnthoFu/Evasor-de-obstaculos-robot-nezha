def on_button_pressed_a():
    neZha.set_motor_speed(neZha.MotorList.M1, 40)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    neZha.stop_motor(neZha.MotorList.M1)
input.on_button_pressed(Button.B, on_button_pressed_b)

objeto = 0
angulo = 95
neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)

def on_forever():
    global objeto, angulo
    basic.show_number(angulo)
    objeto = PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J1,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM)
    if objeto > 5 and objeto >= 20:
        angulo += 40
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)
        basic.pause(2000)
        angulo += -40
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)
basic.forever(on_forever)
