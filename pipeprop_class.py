
import math


# define global variables with densities of steel and water
global DENS_SEAWATER_PSF
global DENS_STEEL_PSF
global DENS_SEAWATER_METRIC
global DENS_STEEL_METRIC
DENS_SEAWATER_PSF = 64.2     # density in pcf
DENS_STEEL_PSF = 490.0       # density in pcf
DENS_SEAWATER_METRIC = 10.085015188800002   # denisty if kN/m^3
DENS_STEEL_METRIC = 76.97285736             # denisty if kN/m^3



class PipeProp:

    def __init__(self, dia, thk, units):
        ''' creates a pipe defined by it's diameter and thickness. The units
        in inches "in" or "mm" needs to be specified so that the units and weights are calculated properly'''

        # for 'dia', only allow positive values. int will be converted to float
        try:
            testdia = float(dia)    # if its a string it will go to except:
            if testdia > 0:
                self.dia = testdia
            else:
                raise Exception('Diameter can only be positive, non-zero value')
        except:
            raise Exception('Diameter can only be positive, non-zero value')

        # for 'thk', only allow positive values. int will be converted to float
        try:
            testthk = float(thk)    # if its a string it will go to except:
            if testthk > 0:
                self.thk = testthk
            else:
                raise Exception('Thickness can only be positive, non-zero value')
        except:
            raise Exception('Thickness can only be positive, non-zero value')

        # only allow 'in' and 'mm' as options for units
        if units in ['in', 'mm']:
            self.units = units
        else:
            raise Exception('Wrong units. Use "in" or "mm"')

    def ID(self):
        '''Determines the inside diameter of the pipe'''
        return self.dia - 2 * self.thk

    def dOverT(self):
        '''Determines the D/t ratio of the pipe'''
        return self.dia/self.thk

    def wgt_per_length(self):
        '''Determines the weight per linear length of the pipe. For "in" unit,
        the weight is provided in lb/ft. For "mm" units, it is provided in kN/m'''
        if self.units == "in":
            wgtperlen = self.area() / 144 * DENS_STEEL_PSF
        else:
            wgtperlen = self.area() / 100**2 * DENS_STEEL_METRIC   # area is calc'd in cm^2
        return wgtperlen

    def displacedArea(self):
        '''Determines the displaced area of the pipe. Assumes the pipe is sealed
        so the entire pipe will displace water if it's under water. for 'in', area is
        provided in in^2. For 'mm', area is provided in cm^2'''
        if self.units == "in":
            pipe_dArea  = (self.dia/2)**2 * math.pi
        else:
            pipe_dArea  = (self.dia/2)**2 * math.pi / 10**2
        return pipe_dArea

    def buoy_per_length(self):
        '''Determines the buoyancy of the pipe per linear length. For "in" units,
        the buoyancy is provided in lb/ft. For "mm" units, it's provide in kN/m.'''
        if self.units == "in":
            buoy  = self.displacedArea() / 144 * DENS_SEAWATER_PSF
        else:
            buoy  = self.displacedArea() / 100**2 * DENS_SEAWATER_METRIC # area is calc'd in cm^2
        return buoy

    def area(self):
        '''Determines the pipe area. For "in" units, it's provided in in^2.
        For "mm" units, it's provided in cm^2'''
        if self.units == "in":
            pipe_area  = math.pi * (self.dia - self.thk) * self.thk
        else:
            pipe_area  = math.pi * (self.dia - self.thk) * self.thk / 10**2
        return pipe_area


    def momtI(self):
        '''Determines the pipe's moment of inertia. For "in" units, it's
        provided in in^4. For "mm" units, it's provided in cm^4.'''
        if self.units == "in":
            pipeM  = math.pi / 64 * (self.dia**4 - (self.dia-self.thk*2)**4)
        else:
            pipeM  = math.pi / 64 * (self.dia**4 - (self.dia-self.thk*2)**4) / 10**4
        return pipeM

    def sectMod(self):
        '''Determines the pipe's section modulus. For "in" units, it's
        provided in in^3. For "mm" units, it's provided in cm^3.'''
        if self.units == "in":
            pipeSM = math.pi / 32 /self.dia * (self.dia**4-(self.dia-self.thk*2)**4)
        else:
            pipeSM = math.pi / 32 /self.dia * (self.dia**4-(self.dia-self.thk*2)**4) / 10**3
        return pipeSM


    def radiusGyration(self):
        '''Determines the pipe's radius of Gyration. For "in" units, it's
        provided in in. For "mm" units, it's provided in cm.'''
        # For 'mm' units, I and A are based on 'cm' so R results in 'cm'
        return math.sqrt(self.momtI() / self.area())


    def pMomtI(self):
        '''Determines the pipe's moment of inertia. For "in" units, it's
        provided in in^4. For "mm" units, it's provided in cm^4.'''
        if self.units == "in":
            pipePM = math.pi / 2 * ((self.dia/2)**4-((self.dia-2*self.thk)/2)**4)
        else:
            pipePM = math.pi / 2 * ((self.dia/2)**4-((self.dia-2*self.thk)/2)**4) / 10**4
        return pipePM

    def circumference(self):
        '''Determines the pipe's circumference. For "in" units, it's
        provided in 'in'. For "mm" units, it's provided in 'cm'.'''
        if self.units == "in":
            pipeCircum = math.pi * self.dia
        else:
            pipeCircum = math.pi * self.dia / 10
        return pipeCircum

    def innerVol_per_length(self):
        '''Determines the pipe's internal volume. For "in" units, it's
        provided in 'ft^3/ft'. For "mm" units, it's provided in 'm^3/m'.'''

        if self.units == "in":
            pipeIVol = math.pi * ((self.dia-2*self.thk)/2)**2 / 144
        else:
            pipeIVol = math.pi * ((self.dia-2*self.thk)/2)**2 / 1000**2
        return pipeIVol


###### TESTING #################################################################
# The following code was used to test the class as it was being written and
# also to create a dictionary with all results for use in unittest file.
#
def test_pipeprop_class(diameter, thickness, units):

    pipe1 = PipeProp(diameter,thickness, units)

    d = {}

    d["Pipe Dia"] = pipe1.dia
    d["Pipe Thk"] = pipe1.thk
    d["Pipe D/t"] = pipe1.dOverT()
    d["Pipe ID"] = pipe1.ID()
    d["Pipe wgt_per_length"] = pipe1.wgt_per_length()
    d["Pipe displacedArea"] = pipe1.displacedArea()
    d["Pipe buoy_per_length"] = pipe1.buoy_per_length()
    d["Pipe Area"] = pipe1.area()
    d["Pipe I"] = pipe1.momtI()
    d["Pipe S"] = pipe1.sectMod()
    d["Pipe r"] = pipe1.radiusGyration()
    d["Pipe J"] = pipe1.pMomtI()
    d["Pipe circumference"] = pipe1.circumference()
    d["Pipe innerVol_per_length"] = pipe1.innerVol_per_length()

    return ( d )


d1 = test_pipeprop_class(30,1,"in")
d2 = test_pipeprop_class(762,25,"mm")

# write out the stuff in the dictionaries so output is brought into
# Excel so it can be compared to the spreadsheet values.

print("")
print("Data for d1 --------------")
print("")
for key in d1.keys():
    print("{}   {}".format(key, d1[key]) )
print("")
print("Data for d2 --------------")
print("")
for key in d2.keys():
    print("{}   {}".format(key, d2[key]) )


print("")
print("")
print("Test Class without creating an object")
print(PipeProp(30,1,"in").area())
