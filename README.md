# Lab Access Management System

A command-line application built in Python using an Object-Oriented MVC architecture. The system allows students to book lab equipment slots and enables lab coordinators to review bookings.

---

## Features

* MVC-based project structure
* In-memory data management (`AppRepo`)
* Student booking workflow
* Lab coordinator review system
* Pre-seeded sample data for testing

---

## Requirements

* Python 3.8+
* No external libraries required

---

## Running the Application

```bash
python main.py
```

---

## Usage

1. Select **Student Login**
2. Enter a valid registration number (e.g., `1`, `2`, `3`)
3. Choose lab, equipment, and timeslot
4. Booking is created
5. Login as a coordinator (IDs: `4`, `5`, `6`) to view bookings

---

## Project Structure

```
lab_access/
├── main.py
├── repo/
│   └── Apprepo.py
├── controllers/
│   ├── StudentController.py
│   └── LabcoorController.py
└── models/
    ├── user.py
    ├── student.py
    ├── labcoordination.py
    ├── lab.py
    ├── equipment.py
    ├── timslot.py
    └── bookslot.py
```

---

## Notes

* Data is stored in memory and resets on each run
* Booking approval logic is not fully implemented
* Basic input handling; no validation or conflict checks

---

## Future Enhancements

* Add database support
* Implement approval workflow
* Improve validation and error handling
* Add unit testing

---

## License

Not specified
