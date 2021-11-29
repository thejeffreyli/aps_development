from ophyd import Device
from ophyd import EpicsSignal
from ophyd import Component as Cpt
from bluesky import plan_stubs as bps

# You should always use this plan, *never* Python’s built-in function :func:`time.sleep`
# import time


class Rigaku500k_Cam1(Device):
    acquire_time = Cpt(EpicsSignal, '8idRigaku:cam1:AcquireTime')
    image_mode = Cpt(EpicsSignal, '8idRigaku:cam1:ImageMode')
    trigger_mode = Cpt(EpicsSignal, '8idRigaku:cam1:TriggerMode')
    num_images = Cpt(EpicsSignal, '8idRigaku:cam1:NumImages')
    corrections = Cpt(EpicsSignal, '8idRigaku:cam1:Corrections')
    data_type = Cpt(EpicsSignal, '8idRigaku:cam1:DataType')


    det_state = Cpt(EpicsSignal, '8idRigaku:cam1:AcquisitionDelay') # <-------- added this
    file_name = Cpt(EpicsSignal, '8idRigaku:cam1:FileName')    
    acquire = Cpt(EpicsSignal, '8idRigaku:cam1:Acquire')  


class Rigaku500k_HDF1(Device):
    acquire_time = Cpt(EpicsSignal, '8idRigaku:HDF1:NumCapture')


class Rigaku500k(Device):
    cam1 = Cpt(Rigaku500k_Cam1)
    hdf1 = Cpt(Rigaku500k_HDF1) # not used


def Rigaku_Fast(rigaku500k):
    yield from bps.mv(rigaku500k.cam1.acquire_time, 30e-6)    
    yield from bps.mv(rigaku500k.cam1.image_mode, 5)   
    yield from bps.mv(rigaku500k.cam1.trigger_mode, 4)   
    yield from bps.mv(rigaku500k.cam1.num_images, 100000)   
    yield from bps.mv(rigaku500k.cam1.corrections, "Enabled")       
    yield from bps.mv(rigaku500k.cam1.data_type, "UInt32")   

    max_repeats=2
    
    # unix('rm -rf /home/8ididata/RigakuEpics/test*')

    for ii in range(0,10):
        for ival in range(1, max_repeats):
        
            _filename= "ZDT{:02d}_{:06d}.bin".format(ii,ival)
            
            while rigaku500k.cam1.det_state != "Idle":
                bps.sleep(0.1)
            print("Start Rigaku Acquire %s\n",_filename)
        
            while rigaku500k.cam1.det_state == "Idle":
                bps.sleep(0.1)
                yield from bps.mv(rigaku500k.cam1.file_name, _filename)       
                yield from bps.mv(rigaku500k.cam1.acquire, 1)                  
                continue
        
            while rigaku500k.cam1.det_state != "Idle":
                bps.sleep(0.1)
    
def main():
    test_object = Rigaku500k(name="test_object")
    Rigaku_Fast(test_object)
    
if __name__ == '__main__':
    main()    
        