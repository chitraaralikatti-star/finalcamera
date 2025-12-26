import os

class CameraManager:
    def __init__(self):
        self.usage = {}

    def book_camera(self, camera, used_hours):
        self.usage[camera] = used_hours

    def booking_decision(self, camera, requested_hours, capacity, priority):
        used_hours = self.usage.get(camera, 0)
        total_hours = used_hours + requested_hours

        if total_hours <= capacity:
            return "APPROVE"
        elif priority == "HIGH" and total_hours <= capacity + 2:
            return "CONDITIONALLY_APPROVE"
        else:
            return "REJECT"

    def best_available_camera(self):
        return min(self.usage, key=self.usage.get)


# ---- Jenkins Execution Entry Point ----
if __name__ == "__main__":
    camera = os.getenv("ENTER_CAMERA")
    used_hours = os.getenv("USED_HOURS")
    requested_hours = os.getenv("REQUESTED_HOURS")
    capacity = os.getenv("CAPACITY")
    priority = os.getenv("PRIORITY")

    if not camera or not used_hours or not requested_hours or not capacity or not priority:
        print("ERROR: Jenkins parameters missing")
        exit(1)

    used_hours = int(used_hours)
    requested_hours = int(requested_hours)
    capacity = int(capacity)

    c = CameraManager()
    c.book_camera(camera, used_hours)

    decision = c.booking_decision(camera, requested_hours, capacity, priority)

    print("Camera:", camera)
    print("Used Hours:", used_hours)
    print("Requested Hours:", requested_hours)
    print("Capacity:", capacity)
    print("Priority:", priority)
    print("Decision:", decision)
