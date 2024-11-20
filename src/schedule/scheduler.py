import os
import json
from datetime import datetime, timedelta


# Đường dẫn tuyệt đối đến file schedule.json
BASE_DIR = os.path.dirname(os.path.abspath("src/database/schedule.json"))
SCHEDULE_FILE = os.path.join(BASE_DIR, "schedule.json")
print(SCHEDULE_FILE)
# Tải lịch từ file hoặc tạo mới nếu chưa tồn tại
def load_schedule(filename=SCHEDULE_FILE):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            return json.loads(data) if data else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        # Trả về dictionary rỗng nếu file không phải JSON hợp lệ
        return {}


# Lưu lịch vào file
def save_schedule(schedule, filename=SCHEDULE_FILE):
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Ghi dữ liệu vào file JSON
    with open(filename, 'w') as file:
        json.dump(schedule, file, indent=4)


# Thêm thời gian biểu và có tùy chọn lặp lại hàng tuần
def add_schedule(username, title, start_time, end_time, date, urgency, importance, note=""):
    # Tải lịch hiện tại
    schedule = load_schedule()
    
    # Kiểm tra nếu chưa có lịch cho username, tạo mới nếu cần
    if username not in schedule:
        schedule[username] = {}


    # Tạo event_id mới cho người dùng này
    user_schedule = schedule[username]
    maxx = 0
    for event_id, event in user_schedule.items():
        if int(event_id) > maxx:
            maxx = int(event_id)
    event_id = maxx + 1
    
    # Thêm sự kiện vào lịch của người dùng
    user_schedule[event_id] = {
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "date": date,
        "urgency": urgency,
        "importance": importance,
        "note": note
    }
    
    # Lưu lại lịch đã chỉnh sửa
    save_schedule(schedule)
    return event_id


# Xóa thời gian biểu của người dùng
def delete_schedule(username, event_id):
    schedule = load_schedule()
    if username in schedule and str(event_id) in schedule[username].keys():
        del schedule[username][str(event_id)]
        save_schedule(schedule)
        return True
    return False


# Lấy thời gian biểu của người dùng cho một ngày hoặc nhiều ngày
def get_schedule(username, date=None, days=1, sort_by=None):
    schedule = load_schedule()
    selected_schedules = []
    
    # Kiểm tra nếu username có lịch
    if username not in schedule:
        return selected_schedules
    
    user_schedule = schedule[username]
    current_time = datetime.now()


    for event_id, event in user_schedule.items():
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if date:
            selected_date = datetime.strptime(date, "%Y-%m-%d")
            if selected_date <= event_date < selected_date + timedelta(days=days):
                event_with_id = {"ID": event_id}  # Thêm ID vào sự kiện
                event_with_id.update(event)
                selected_schedules.append(event_with_id)
        else:
            event_with_id = {"ID": event_id}
            event_with_id.update(event)
            selected_schedules.append(event_with_id)
    
    # Sắp xếp các sự kiện theo thời gian gần nhất hiện tại hoặc theo mức độ khẩn cấp và quan trọng
    if sort_by == "urgency":
        selected_schedules.sort(key=lambda x: x["urgency"], reverse=True)
    elif sort_by == "importance":
        selected_schedules.sort(key=lambda x: x["importance"], reverse=True)
    else:
        selected_schedules.sort(key=lambda x: datetime.strptime(x["date"] + " " + x["start_time"], "%Y-%m-%d %H:%M"))
    
    return selected_schedules
