from tkinter import *
from tkinter import Button
import math

#********************************************prrf block************************************************************
def prrf():
    root1 = Tk()
    root1.title("Rolling Resistance Force:")
    root1.geometry("750x450")
    root1['bg'] = 'lemon chiffon'

    def prrf2():
        global prr_label
        fwr1 = f1.get()
        fwr2 = f2.get()
        Px = P.get()
        Vx = V.get()
        mass = m.get()
        fr = fr1.get()
        if fwr1 == fwr2:
            Fx = (float(Px) * 1000) / ((float(Vx) * 1000) / 3600)
            froll = (float(fr) * float(mass) * float(fwr1) / 10) * 9.8
            Prr = round(((float(froll) * 2) / float(Fx) * 100),2)
            prr_label = Label(root1,text="Answer:The Rolling Resistance Force(in N) is : "+str(Prr),
                                font=("Times New Roman", 14))
            prr_label.grid(row=12, column=0)



        else:
            Fx = (float(Px) * 1000) / ((float(Vx) * 1000) / 3600)
            froll1 = (float(fr) * float(mass) * float(fwr1) / 10) * 9.8
            froll2 = (float(fr) * float(mass) * float(fwr2) / 10) * 9.8
            Prr = round(((float(froll1) + float(froll2)) / float(Fx)),2)
            prr_label = Label(root1, text="Answer: The Rolling Resistance Force(in N) is :"+str(Prr),
                              font=("Times New Roman", 14))
            prr_label.grid(row=12, column=0)

    def clear():
        f1.delete(0, 'end')
        f2.delete(0, 'end')
        P.delete(0, 'end')
        V.delete(0, 'end')
        m.delete(0, 'end')
        fr1.delete(0, 'end')
        prr_label.grid_forget()
    # To ask for the mass of vehicle
    mass1_label = Label(root1, text="Enter Mass Of Vehicle(in kg): ", font=("Times New Roman", 12))
    mass1_label.grid(row=4, column=0,sticky=W, pady=10, padx=0)

    # To Enter the value of vehicle
    m = Entry(root1, width=20, font=("Helvitica", 12))
    m.grid(row=4, column=1, pady=10, padx=0)

    # To ask for value of  rolling resistance coefficient
    fr1_label = Label(root1, text="Enter Rolling Resistance Coefficient: ", font=("Times New Roman", 12))
    fr1_label.grid(row=5, column=0,sticky=W, pady=10, padx=0)

    # To Enter the value of rolling resistance coefficient
    fr1 = Entry(root1, width=20, font=("Helvitica", 12))
    fr1.grid(row=5, column=1, pady=10, padx=0)
    # To ask for the weight distribution of front wheel
    fwr1_label = Label(root1, text="Enter Weight Distribution Of Front Wheel(out of 10): ", font=("Times New Roman", 12))
    fwr1_label.grid(row=6, column=0, pady=10, sticky=W, padx=0)
    # To enter weight distribution of rear wheel
    f1 = Entry(root1, width=20, font=("Helvitica", 12))
    f1.grid(row=6, column=1, pady=10, padx=0)
    # To ask for the weight distribution of rear wheel
    fwr2_label = Label(root1, text="Enter Weight Distribution Of Rear Wheel(out of 10): ", font=("Times New Roman", 12))
    fwr2_label.grid(row=7, column=0, pady=10, sticky=W, padx=0)
    # To enter weight distribution of rear wheel
    f2 = Entry(root1, width=20, font=("Helvitica", 12))
    f2.grid(row=7, column=1, pady=10, padx=0)
    # To ask for the speed of vehicle
    vs1_label = Label(root1, text="Enter Speed Of The Vehicle(in kmph) : ", font=("Times New Roman", 12))
    vs1_label.grid(row=8, column=0, pady=10, sticky=W, padx=0)
    # To enter the speed of vehicle
    V = Entry(root1, width=20, font=("Helvitica", 12))
    V.grid(row=8, column=1, pady=10, padx=0)
    # To ask for the traction power
    tp1_label = Label(root1, text="Enter Traction Power(in kW) : ", font=("Times New Roman", 12))
    tp1_label.grid(row=9, column=0, pady=10, sticky=W, padx=0)
    # To enter the traction power
    P = Entry(root1, width=20, font=("Helvitica", 12))
    P.grid(row=9, column=1, pady=10, padx=0)
    Prrf2_button = Button(root1, text=" Calculate Rolling Resistance Force",bd='8', command=prrf2)
    Prrf2_button.grid(row=10, column=1, pady=0)
    clear_button = Button(root1, text="Clear",bd='8', command=clear)
    clear_button.grid(row=11, column=1, pady=0)
#**********************************************************ltf block**************************************************
def ltf():
    root2 = Tk()
    root2.title("Longitudinal traction force:")
    root2.geometry("750x400")
    root2['bg'] = 'lemon chiffon'

    def ltf2():
        global fx_label
        Us = us.get()
        slip = s.get()
        m1 = m.get()
        Fx = round((float(Us) * float(slip) * float(m1) * 9.8),2)
        fx_label = Label(root2, text="Answer: The Value Of Longitudinal Traction Force(in kN): " +str(Fx),font=("Garamond", 14))
        fx_label.grid(row=12, column=0)
    def clear():
        us.delete(0, 'end')
        s.delete(0, 'end')
        m.delete(0, 'end')
        fx_label.grid_forget()

    # To ask for the mass of vehicle
    us1_label = Label(root2, text="Enter longitudinal Friction Coefficient: ", font=("Times New Roman", 12))
    us1_label.grid(row=4, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    us= Entry(root2, width=20, font=("Helvitica", 12))
    us.grid(row=4, column=1,sticky=W, pady=10, padx=25)

    # To ask for value of  slip
    slip_label = Label(root2, text="Enter Value Of Slip:", font=("Times New Roman", 12))
    slip_label.grid(row=5, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of slip
    s = Entry(root2, width=20, font=("Helvitica", 12))
    s.grid(row=5, column=1, pady=10, padx=25)
    mass1_label = Label(root2, text="Enter Mass Of Vehicle(in kg): ", font=("Times New Roman", 12))
    mass1_label.grid(row=6, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of mass of vehicle
    m = Entry(root2, width=20, font=("Helvitica", 12))
    m.grid(row=6, column=1, pady=10, padx=25)

    ltf2_button = Button(root2, text=" Calculate Longitudinal Traction force",bd='8', command=ltf2)
    ltf2_button.grid(row=10, column=1,sticky=W, pady=5)
    clear_button = Button(root2, text="Clear",bd='8', command=clear)
    clear_button.grid(row=11, column=1, pady=5)
#**********************************************************ltf block**************************************************
#**********************************************************roadl block**************************************************
def roadl():
    root3 = Tk()
    root3.title("Road Load:")
    root3.geometry("750x400")
    root3['bg'] = 'lemon chiffon'

    def roadl2():
        global fx_label
        Fr1 = fr.get()
        rg = rg1.get()
        m2 = m.get()
        a = math.atan(float(rg))
        Fx1 = round((float(Fr1) * float(m2) * 9.8 *math.cos(float(a)) + float(m2) * 9.8 * math.sin(float(a))),2)
        fx_label = Label(root3, text="Answer: The Value Of Road Load (in N) is : " +str(Fx1),font=("Times New Roman", 14))
        fx_label.grid(row=12, column=0)

    def clear():
            fr.delete(0, 'end')
            rg1.delete(0, 'end')
            m.delete(0, 'end')
            fx_label.grid_forget()


    # To ask for the mass of vehicle
    Fr11_label = Label(root3, text="Enter Rolling Resistance Coefficient: ", font=("Times New Roman", 12))
    Fr11_label.grid(row=4, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    fr= Entry(root3, width=20, font=("Helvitica", 12))
    fr.grid(row=4, column=1, pady=10, padx=25)

    # To ask for value of  rolling resistance coefficient
    rg11_label = Label(root3, text="Enter Road Grade(in %):", font=("Times New Roman", 12))
    rg11_label.grid(row=5, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of rolling resistance coefficient
    rg1 = Entry(root3, width=20, font=("Helvitica", 12))
    rg1.grid(row=5, column=1, pady=10, padx=25)
    mass1_label = Label(root3, text="Enter Mass Of Vehicle(in kg): ", font=("Times New Roman", 12))
    mass1_label.grid(row=6, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    m = Entry(root3, width=20, font=("Helvitica", 12))
    m.grid(row=6, column=1, pady=10, padx=25)

    road2_button = Button(root3, text="Road Load",bd='8', command=roadl2)
    road2_button.grid(row=10, column=1, pady=5)
    clear_button = Button(root3, text="Clear",bd='8', command=clear)
    clear_button.grid(row=11, column=1, pady=5)
#**********************************************************raodl block**************************************************
#**********************************************************motorp block**************************************************
def motorp():
    root4 = Tk()
    root4.title("Motor Power:")
    root4.geometry("750x400")
    root4['bg'] = 'lemon chiffon'

    def motorp2():
        global pe_label
        Fr1 = fr.get()
        rg = rg1.get()
        nf=nf1.get()
        m2 = m.get()
        Vx=V.get()
        a = math.atan(float(rg))
        Fx1 = float(Fr1) * float(m2) * 9.8 * float(math.cos(a)) + ((float(m2) * 9.8 * math.sin(a)))
        Pe = round((float(Fx1) * float (Vx) * 1000 / 3600 / float(nf)),2)
        pe_label = Label(root4, text="Answer: The Value Of Motor Power (in kW): " +str(Pe),font=("Times New Roman", 14))
        pe_label.grid(row=12, column=0)

    def clear():
        fr.delete(0, 'end')
        rg1.delete(0, 'end')
        nf1.delete(0, 'end')
        m.delete(0, 'end')
        V.delete(0, 'end')
        pe_label.grid_forget()

    # To ask for the mass of vehicle
    Fr11_label = Label(root4, text="Enter Rolling Resistance Coefficient: ", font=("Times New Roman", 12))
    Fr11_label.grid(row=4, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    fr= Entry(root4, width=20, font=("Helvitica", 12))
    fr.grid(row=4, column=1, pady=10, padx=25)

    # To ask for value of  rolling resistance coefficient
    rg11_label = Label(root4, text="Enter Road Grade(in %) :", font=("Times New Roman", 12))
    rg11_label.grid(row=5, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of rolling resistance coefficient
    rg1 = Entry(root4, width=20, font=("Helvitica", 12))
    rg1.grid(row=5, column=1, pady=10, padx=25)
    mass1_label = Label(root4, text="Enter Mass Of Vehicle (in kg): ", font=("Times New Roman", 12))
    mass1_label.grid(row=6, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    m = Entry(root4, width=20, font=("Helvitica", 12))
    m.grid(row=6, column=1, pady=10, padx=25)


    vs1_label = Label(root4, text="Enter Speed Of The Vehicle(in kmph) : ", font=("Times New Roman", 12))
    vs1_label.grid(row=7, column=0, pady=10, sticky=W, padx=5)
    # To enter the speed of vehicle
    V = Entry(root4, width=20, font=("Helvitica", 12))
    V.grid(row=7, column=1, pady=10, padx=25)
    nf11_label = Label(root4, text="Enter The Drive Line Efficiency: ", font=("Times New Roman", 12))
    nf11_label.grid(row=8, column=0, pady=10, sticky=W, padx=5)
    # To enter the speed of vehicle
    nf1= Entry(root4, width=20, font=("Helvitica", 12))
    nf1.grid(row=8, column=1, pady=10, padx=25)
    mp2_button = Button(root4, text="Motor Power",bd='8', command=motorp2)
    mp2_button.grid(row=9, column=1, pady=5)
    clear_button = Button(root4, text="Clear",bd='8', command=clear)
    clear_button.grid(row=11, column=1, pady=5)

#**********************************************************motorp block**************************************************
#**********************************************************gdr block**************************************************
def gdr1():
    root5 = Tk()
    root5.title("Gear Ratio:")
    root5.geometry("750x400")
    root5['bg'] = 'lemon chiffon'

    def gdr2():
        global gdrr_label
        rw = rw1.get()
        wr = wr1.get()
        Vx=V.get()
        slip=s.get()
        gdr = round(((float(wr) /float (Vx)) * float(rw) * (1 - float(slip))),2)
        gdrr_label = Label(root5, text="Answer: The Value Of Gear Ratio is: " +str(gdr),font=("Garamond", 14))
        gdrr_label.grid(row=12, column=0)
    def clear():
        rw1.delete(0, 'end')
        wr1.delete(0, 'end')
        V.delete(0, 'end')
        s.delete(0, 'end')
        gdrr_label.grid_forget()

    # To ask for the mass of vehicle
    rw11_label = Label(root5, text="Enter The Wheel Dynamic Rolling Radius(in m): ", font=("Garamond", 12))
    rw11_label.grid(row=4, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    rw1= Entry(root5, width=20, font=("Helvitica", 12))
    rw1.grid(row=4, column=1, pady=10, padx=25)

    # To ask for value of  rolling resistance coefficient
    wr11_label = Label(root5, text="Enter The Motor Speed(in RPM):", font=("Garamond", 12))
    wr11_label.grid(row=5, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of rolling resistance coefficient
    wr1 = Entry(root5, width=20, font=("Helvitica", 12))
    wr1.grid(row=5, column=1, pady=10, padx=25)

    vs1_label = Label(root5, text="Enter Speed Of The Vehicle(in kmph) : ", font=("Garamond", 12))
    vs1_label.grid(row=7, column=0, pady=10,sticky=W, padx=5)
    # To enter the speed of vehicle
    V = Entry(root5, width=20, font=("Helvitica", 12))
    V.grid(row=7, column=1, pady=10, padx=25)
    # To ask for value of  slip
    slip_label = Label(root5, text="Enter Value Of Slip:", font=("Garamond", 12))
    slip_label.grid(row=6, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of slip
    s = Entry(root5, width=20, font=("Helvitica", 12))
    s.grid(row=6, column=1, pady=10, padx=25)


    gdr3_button = Button(root5, text="Gear Ratio",bd='8', command=gdr2)
    gdr3_button.grid(row=9, column=1, pady=5)
    clear_button = Button(root5, text="Clear",bd='8', command=clear)
    clear_button.grid(row=10, column=1, pady=5)

#**********************************************************gdr block**************************************************
#**********************************************************adf block**************************************************
def adf():
    root6 = Tk()
    root6.title("Aerodynamic Drag Force:")
    root6.geometry("750x400")
    root6['bg'] = 'lemon chiffon'

    def adf2():
        global faero_label
        md = 1.225
        Cd = cd1.get()
        Af=af.get()
        Vx=V.get()
        Vw=V1.get()
        Faero = round((float(md) * float(Cd) *float (Af) / 2) * ((float(Vx) + float(Vw)) ** 2),2)
        faero_label = Label(root6, text="Answer: The Value Of Aerodynamic Drag Force(in N): " +str(Faero),font=("Times New Roman", 14))
        faero_label.grid(row=12, column=0)

    def clear():
            cd1.delete(0, 'end')
            af.delete(0, 'end')
            V1.delete(0, 'end')
            V.delete(0, 'end')
            faero_label.grid_forget()

    # To ask for the mass of vehicle
    cd11_label = Label(root6, text="Enter The Aerodynamic Drag Coefficient: ", font=("Times New Roman", 12))
    cd11_label.grid(row=4, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of vehicle
    cd1= Entry(root6, width=20, font=("Helvitica", 12))
    cd1.grid(row=4, column=1, pady=10, padx=25)

    # To ask for value of  rolling resistance coefficient
    af11_label = Label(root6, text="Enter Frontal Area(in m^2):", font=("Times New Roman", 12))
    af11_label.grid(row=5, column=0,sticky=W, pady=10, padx=5)

    # To Enter the value of rolling resistance coefficient
    af = Entry(root6, width=20, font=("Helvitica", 12))
    af.grid(row=5, column=1, pady=10, padx=25)

    vs1_label = Label(root6, text="Enter Speed Of The Vehicle(in kmph) : ", font=("Times New Roman", 12))
    vs1_label.grid(row=7, column=0, pady=10, sticky=W, padx=5)
    # To enter the speed of vehicle
    V = Entry(root6, width=20, font=("Helvitica", 12))
    V.grid(row=7, column=1, pady=10, padx=25)
    vs11_label = Label(root6, text="Enter The Headwind Speed(in kmph): ", font=("Times New Roman", 12))
    vs11_label.grid(row=8, column=0, pady=10, sticky=W, padx=5)
    # To enter the speed of vehicle
    V1 = Entry(root6, width=20, font=("Helvitica", 12))
    V1.grid(row=8, column=1, pady=10, padx=25)


    adff_button = Button(root6, text="Aerodynamic Drag Force",bd='8', command=adf2)
    adff_button.grid(row=9, column=1, pady=5)
    clear_button = Button(root6, text="Clear",bd='8', command=clear)
    clear_button.grid(row=10, column=1, pady=5)

#**********************************************************adf block**************************************************
# **********************************************************landing block**************************************************
def landing():
    root = Tk()
    root.title("Electric Vehicle Analysis")
    root.geometry("710x550")
    root['bg'] = 'light blue'

    # To display name of college
    project = Label(root, text="*******Welcome To Analysis Of Electric Vehicle*******", font=("Lucida Fax", 20))
    project.grid(row=0, column=0, pady=5, padx=5)

    # To display choice for user
    question = Label(root, bg='light green', text="WHAT WOULD YOU LIKE TO CALCULATE?", font=("Gadugi"))
    question.grid(row=2, column=0, pady=3)

    prrf1_button = Button(root, text="Rolling Resistance Force", bg='azure',bd='8', command=prrf)
    prrf1_button.grid(row=7, column=0, pady=5)
    ltf_button = Button(root, text="Longitudinal Traction Force", bg='azure',bd='8', command=ltf)
    ltf_button.grid(row=8, column=0, pady=5)
    roadl_button = Button(root, text="Road Load", bg='azure',bd='8', command=roadl)
    roadl_button.grid(row=9, column=0, pady=5)
    motorp_button = Button(root, text="Motor Power", bg='azure',bd='8', command=motorp)
    motorp_button.grid(row=10, column=0, pady=5)
    adf_button = Button(root, text="Aerodynamic Drag Force", bg='azure',bd='8', command=adf)
    adf_button.grid(row=11, column=0, pady=5)
    gearr_button = Button(root, text="Gear Ratio", bg='azure',bd='8', command=gdr1)
    gearr_button.grid(row=12, column=0, pady=5)

    destroy_button = Button(root, text="Quit", bg='coral',bd='8', command=root.destroy)
    destroy_button.grid(row=13, column=0, pady=5)


# **********************************************************landing block**************************************************
root0 = Tk()

# Adjust size
root0.geometry("900x900")
root0.title("Analysis Of Electric Vehicle:")

# Add image file
bg = PhotoImage(file="NNec11.png")

# Create Canvas
canvas1 = Canvas(root0, width=900,
                 height=900)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")
canvas1.create_text(450,30, text="SHRI RAMDEOBABA COLLEGE OF ENGINEERING AND MANAGEMENT",fill="white",font=("Lucida Fax", 18))
canvas1.create_text(450,65, text="ELECTRICAL ENGINEERING DEPARTMENT",fill="white",font=("Lucida Fax", 18))
canvas1.create_text(440,100, text="ANALYSIS OF ELECTRIC VEHICLE ",fill="lime",font=("Lucida Fax", 16))
canvas1.create_text(440,140, text="USING PYTHON AND TKINTER",fill="coral",font=("Lucida Fax", 16))
# Create Buttons
button1 = Button(root0, text="EXIT",bd='10',bg='coral', command=root0.destroy)
button2 = Button(root0, text="Let's Get Started",bd='10',width=40,command=landing)


# Display Buttons
button1_canvas = canvas1.create_window(430,360,anchor="n",window=button1)
button2_canvas = canvas1.create_window(280,300, anchor="nw",window=button2)

root0.mainloop()

