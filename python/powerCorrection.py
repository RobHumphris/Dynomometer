from math import exp

# From http://www.scielo.br/pdf/jbsmse/v25n3/a10v25n3.pdf
# SAE J 1349 Power Correction Factor
# (990/Pd)*(((Tc+273)/298)^0.5)
#    Pd = the pressure of the dry air, mb
#    Tc = ambient temperature, deg C
#

# Takes Temperature °C returns Water Vapour Pressure in kpa
def waterpressure(Tc):
    kpa = 0.61121 * exp((18.678 - Tc / 234.5)*(Tc / (257.14 + Tc)))
    return kpa

# ISO 1585 Power Correction Factor
#   [(p - pv)/(po - pvo)]^1.3 * (To/T)^0.6
#   po = 1000mbar
#   To = 298K (25C)
#   pvo = 10mbar
def ISO1585CorrectionFactor(p, T):
    pv = waterpressure(T)
    return (((p - pv) / 990)**1.3)*((298/(T+273))**0.6)

def SAE1349CorrectionFactor(p, T):
    return -1

def buckTests():
    for t in range(0, 50, 5):
        print("Buck equation, T:" + str(t) + "°C P: " + str(waterpressure(t)) + "mbar")

def correctionTests():
    for p in range(980, 1020, 2):
        print("P=" + str(p) + "mbar. ")
        for t in range(0, 50, 5):
            print(" T=" + str(t) + " cf=" + str(ISO1585CorrectionFactor(p, t)))

buckTests()
correctionTests()