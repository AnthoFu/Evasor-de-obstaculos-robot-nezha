input.onButtonPressed(Button.A, function () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 40)
})
input.onButtonPressed(Button.B, function () {
    neZha.stopMotor(neZha.MotorList.M1)
})
let objeto = 0
let angulo = 95
neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)
basic.forever(function () {
    basic.showNumber(angulo)
    objeto = PlanetX_Basic.ultrasoundSensor(PlanetX_Basic.DigitalRJPin.J1, PlanetX_Basic.Distance_Unit_List.Distance_Unit_cm)
    if (objeto > 5 && objeto >= 20) {
        angulo += 40
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)
        basic.pause(2000)
        angulo += -40
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, angulo)
    }
})
