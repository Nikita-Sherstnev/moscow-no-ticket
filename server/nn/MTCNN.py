from PIL import ImageDraw


def detect_faces_on_frame(frame, nn):
    '''
    Returns list of lists of coordinates.
    '''

    boxes, _ = nn.detect(frame)

    return boxes


def draw_faces(boxes, frame):
    '''
    Draws faces, returns frame
    '''
    frame_draw = frame.copy()
    draw = ImageDraw.Draw(frame_draw)

    for box in boxes:
        draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)

    return frame_draw