# Network-status-notification-system
Network status notification system


firebase = firebase.FirebaseApplication('ใส่ URL Firebase ที่นี่', None) # URL Firebase
def update_Status():
    stat = "Good"   # สถานะแสดงอินเทอร์เน็ต
    firebase.put('Network 001','status',{'status':stat})
    print('Update Status')
def sent_Location():
    link = "ใส่ URL Google Location ที่นี่" # Google Location
    firebase.put('Network 001','location',{'link':link})
    print('Sent Location')
def update_timestamp(): 
    ts = time.time()    # อัพเดทค่าเวลา หมายเหตุ ค่าเวลาขึ้นอยู่กับเครื่อง Raspberry pi3 ที่ใช้ปัจจุบัน
    ts = int(ts)*1000
    print(ts)
    firebase.put('Network 001','timestamp',{'now':ts}) #ค่าเวลาที่ส่งขึ้นไปยัง firebase

while True:
    try:
        sent_Location()
        update_timestamp()
        update_Status()
    except:
        print("Error Network, Can't sent data to Firebase.")
    sleep(60)
