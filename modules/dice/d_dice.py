class Dice:
    def __init__(self, faces : int = 6, interval : int = 1):
        if isinstance(faces, int):
            if faces > 1:
                if interval != 0:
                    if isinstance(interval, int):
                        if isinstance(faces, int):
                            self.faces = faces
                            self.interval = interval
                            self.faces_values = {}

                            self.current_face = 0
                            self.current_value = 0
                            self.current_face_value = {}

                            for i in range(faces):
                                self.faces_values[i + 1] = (i + 1) * self.interval
                            
                            self.current_face_value = {self.current_face : self.current_value}
                        else:
                            raise TypeError("GWS: Faces must be a normal number")
                    else:
                        raise ValueError("GWS: Interval must be a normal number")
                else:
                    raise ValueError("GWS: Interval cannot be 0")
            else:
                raise ValueError("GWS: Dice cannot have less than 1 face")
        else:
            raise TypeError("GWS: Faces must be a number")

    
