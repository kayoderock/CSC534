import turtle
import math


class Triangle :
    def __init__(self,vertices):
        self.vertices = vertices

    def translateCordinate(oldCordinate, transitionDistance):
        cordinate = []
        
        for i in range(2):
            point = (1 - i)*(oldCordinate[0]) + i * oldCordinate[1] + transitionDistance[i] * (1)
            cordinate.append(point)

        return tuple(cordinate)

    def translate (self, transitionDistance):
        newPosition = []

        for i in range(3):
            newPosition.append(translateCordinate(selfVertices[i],transitionDistance))
                    
        self.vertices = newPosition;
        
    def __rotateCordinate__(oldCordinate, rotationAngle):
        x = math.cos(rotationAngle)*(oldCordinate[0]) - math.sin(rotationAngle)*(oldCordinate[1])
        y = math.sin(rotationAngle)*(oldCordinate[0]) + math.cos(rotationAngle)*(oldCordinate[1])
        
        return (x,y)
    
        
    def rotate (self, angle):
        newPosition = []

        for i in range(3):
            newPosition.append(rotateCordinate(selfVertices[i],angle))
                    
        self.vertices = newPosition;
        
        return self.vertices

    
    def draw ():
        return null;
