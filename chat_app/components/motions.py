from reflex_motion import motion
import reflex as rx
def motions(*args, tap_scale = 0.95, hover_scale = 1.01, **kwargs, ):


    return motion(
        *args,
        **kwargs,
        while_hover={
            "scale":hover_scale,
        },
        while_tap={
            "scale": tap_scale
        },
        transition={
            "type": "spring", 
            "stiffness": 400, 
            "damping": 17
        },
        
        
    )