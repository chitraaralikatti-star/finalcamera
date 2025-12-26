from camera import CameraManager

def test_approve():
    c = CameraManager()
    c.book_camera("Camera-A", 3)
    assert c.booking_decision("Camera-A", 2, 8, "LOW") == "APPROVE"

def test_conditionally_approve():
    c = CameraManager()
    c.book_camera("Camera-B", 6)
    assert c.booking_decision("Camera-B", 3, 8, "HIGH") == "CONDITIONALLY_APPROVE"

def test_reject():
    c = CameraManager()
    c.book_camera("Camera-C", 6)
    assert c.booking_decision("Camera-C", 4, 8, "LOW") == "REJECT"

def test_best_camera():
    c = CameraManager()
    c.book_camera("Camera-A", 5)
    c.book_camera("Camera-B", 2)
    assert c.best_available_camera() == "Camera-B"
