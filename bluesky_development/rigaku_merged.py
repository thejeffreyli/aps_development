from ophyd import Device
from ophyd import EpicsSignal
from ophyd import Component as Cpt
from bluesky import plan_stubs as bps

# merged class
class Rigaku500k_Merged(Device):
    
    # CAM1
    acquire_time = Cpt(EpicsSignal, '8idRigaku:cam1:AcquireTime')
    image_mode = Cpt(EpicsSignal, '8idRigaku:cam1:ImageMode')
    trigger_mode = Cpt(EpicsSignal, '8idRigaku:cam1:TriggerMode')
    num_images = Cpt(EpicsSignal, '8idRigaku:cam1:NumImages')
    corrections = Cpt(EpicsSignal, '8idRigaku:cam1:Corrections')
    data_type = Cpt(EpicsSignal, '8idRigaku:cam1:DataType')
    
    det_state = Cpt(EpicsSignal, '8idRigaku:cam1:AcquisitionDelay') 
    cam_file_name = Cpt(EpicsSignal, '8idRigaku:cam1:FileName')    
    acquire = Cpt(EpicsSignal, '8idRigaku:cam1:Acquire')  
    num_que_arrays = Cpt(EpicsSignal, '8idRigaku:cam1:NumQueuedArrays') 


    # HDF1
    auto_inc = Cpt(EpicsSignal, '8idRigaku:HDF1:AutoIncrement') 
    num_capture = Cpt(EpicsSignal, '8idRigaku:HDF1:NumCapture')
    hdf_file_name = Cpt(EpicsSignal, '8idRigaku:HDF1:FileName')
    file_num = Cpt(EpicsSignal, '8idRigaku:HDF1:FileNumber')
    capture = Cpt(EpicsSignal, '8idRigaku:HDF1:Capture_RBV')


# object
class Rigaku500k(Device):
    cam1 = Cpt(Rigaku500k_Merged)

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
                yield from bps.mv(rigaku500k.cam1.cam_file_name, _filename)       
                yield from bps.mv(rigaku500k.cam1.acquire, 1)                  
                continue
        
            while rigaku500k.cam1.det_state != "Idle":
                bps.sleep(0.1)
    
    
    
def Rigaku_Slow(rigaku500k):
    
    # unix('rm -rf /home/8ididata/RigakuEpics/test*')
    
    yield from bps.mv(rigaku500k.cam1.image_mode, "16 Bit, 1S")      
    yield from bps.mv(rigaku500k.cam1.trigger_mode, "Fixed Time")          
    yield from bps.mv(rigaku500k.cam1.data_type, "UInt16")          
    yield from bps.mv(rigaku500k.cam1.auto_inc, "Yes")          
    
    max_repeats=10
    number_of_frames=10000
    
    yield from bps.mv(rigaku500k.cam1.num_images, number_of_frames)          
    yield from bps.mv(rigaku500k.cam1.num_capture, number_of_frames)        
    
        
    # Test t0 = 0.001 s
    acq_t = 0.001
   
    yield from bps.mv(rigaku500k.cam1.acquire_time, acq_t)    
    
    for ival in range(0,max_repeats):

        _filename= "test_{:03d}ms_{:02d}.bin".format(acq_t*1000,ival)
        
        # unix('date')
            
        print("Start Rigaku %s\n",_filename)
        
        yield from bps.mv(rigaku500k.cam1.hdf_file_name, _filename)
        yield from bps.mv(rigaku500k.cam1.file_num, 1)
        yield from bps.mv(rigaku500k.cam1.capture, 1)
        
        bps.sleep(0.05)
            
        if rigaku500k.cam1.det_state == "Idle":
            yield from bps.mv(rigaku500k.cam1.acquire, 1)  
            bps.sleep(0.1)
            
        while rigaku500k.cam1.capture != "Done":
            bps.sleep(0.1)
        
        while rigaku500k.cam1.num_que_arrays > 0:        
            bps.sleep(0.1)
            
        # unix('date')            
        print("\n")  


def main():
    test_object = Rigaku500k(name="test_object")
    Rigaku_Fast(test_object)
    Rigaku_Slow(test_object)
    
if __name__ == '__main__':
    main()    
        
        
        