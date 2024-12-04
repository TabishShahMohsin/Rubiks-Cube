cube={"front":["w","w","w","w","w","w","w","w","w"],
"top":["g","g","g","g","g","g","g","g","g"],
"right":["o","o","o","o","o","o","o","o","o"],
"left":["r", "r","r","r","r","r","r","r","r"],
"bottom":["b","b","b","b","b","b","b","b","b"],
"back":["y","y","y","y","y","y","y","y","y"]}

def up(cube):
    dummy=cube["front"][0:3]
    cube["front"][0:3]=cube['right'][0:3]
    cube["right"][0:3]=cube['back'][0:3]
    cube["back"][0:3]=cube['left'][0:3]
    cube["left"][0:3]=dummy
    
    dummy2=cube["top"][0:3]
    cube["top"][0:3]=cube["top"][:6:-3]
    cube["top"][:6:-3]=cube["top"][7::-1]
    cube["top"][7::-1]=cube["top"][3::3]
    cube["top"][3::3]=dummy2

    
    
    return cube

print(up(cube))


# Can use laptop with arduino to send and recieve data hence sending the desired algorithm to perform onto the Rubik's cube
# Would need 6 servos 
    # Don't go for MG996R
    # Preferabbly go for a continous 360 motor that can go through multiple rounds
    # Also check for data sheet to check for ohmic resistance to determine torque
    # 	A4988/DRV8825 Driver
    # Also match the current rating of the driver and the stepper motor
    