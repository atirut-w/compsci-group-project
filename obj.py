class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> "Vector3":
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> "Vector3":
        return Vector3(self.x / other, self.y / other, self.z / other)


class Obj:
    def __init__(self) -> None:
        self.vertices: list[Vector3] = []

    @classmethod
    def from_file(cls, path: str) -> "Obj":
        obj = cls()

        with open(path, "r") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("#"):
                continue

            parts = line.split(" ")

            match parts[0]:
                case "v":
                    obj.vertices.append(Vector3(parts[1], parts[2], parts[3]))

        return obj
