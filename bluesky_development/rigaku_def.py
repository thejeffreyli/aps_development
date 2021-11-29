
from ophyd import Device
from ophyd import EpicsSignal
from ophyd import Component as Cpt
from bluesky import plan_stubs as bps

# Could you rewrite the rigaku_fast.do I sent earlier using this definition? 
# So basically 8idRigaku:cam1:AcquireTime will become rigaku500k.cam1.acquire_time 
# and similarly for other PVs, and epics_put will become yield from bps.mv, 
# but the rest of the logic are pretty much the same


class Rigaku500k_Cam1(Device):
    acquire_time = Cpt(EpicsSignal, '8idRigaku:cam1:AcquireTime')
    image_mode = Cpt(EpicsSignal, '8idRigaku:cam1:ImageMode')
    trigger_mode = Cpt(EpicsSignal, '8idRigaku:cam1:TriggerMode')
    num_images = Cpt(EpicsSignal, '8idRigaku:cam1:NumImages')
    corrections = Cpt(EpicsSignal, '8idRigaku:cam1:Corrections')
    data_type = Cpt(EpicsSignal, '8idRigaku:cam1:DataType')

class Rigaku500k_HDF1(Device):
    acquire_time = Cpt(EpicsSignal, '8idRigaku:HDF1:NumCapture')


class Rigaku500k(Device):
    cam1 = Cpt(Rigaku500k_Cam1)
    hdf1 = Cpt(Rigaku500k_HDF1)


rigaku500k = Rigaku500k(name="rigaku500k")





