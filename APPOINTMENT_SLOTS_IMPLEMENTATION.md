# Appointment Slots Implementation

## Overview
This document describes the appointment slot management system that allows doctors to manage their availability and patients to book appointments from available slots.

## Features Implemented

### For Doctors:

1. **Manage Availability**
   - Set weekly availability by selecting days of the week
   - Define working hours for each day (start time and end time)
   - Toggle availability on/off without deleting the schedule
   - Access via: `/doctor/manage-availability/`

2. **Manage Appointment Slots**
   - Create custom appointment slots with specific date, time, and duration
   - Set maximum number of patients per slot
   - Mark slots as booked/available
   - Delete unwanted slots
   - Access via: `/doctor/manage-slots/`

3. **Manage Days Off**
   - Schedule days off to block all appointments on specific dates
   - Provide reasons for days off (optional)
   - Automatically cancels all appointments on days off when created
   - Delete days off to re-enable appointments
   - Access via: `/doctor/manage-days-off/`

### For Patients:

1. **Book Appointments with Slot Selection**
   - Select appointment date from available dates
   - Choose from available time slots for the selected date
   - Only see slots that are not fully booked
   - Slots respect doctor's availability and days off
   - Access via: `/book-appointment/<service_id>/`

## Database Models

### DoctorAvailability
- Stores doctor's regular weekly schedule
- Fields: doctor, day_of_week, start_time, end_time, is_available
- Allows doctors to set recurring availability

### AppointmentSlot
- Stores specific appointment time slots
- Fields: doctor, date, start_time, end_time, max_patients, current_bookings, is_available
- Tracks how many patients have booked each slot
- Automatically marks as unavailable when max_patients is reached

### DayOff
- Stores doctor's days off
- Fields: doctor, date, reason
- Automatically cancels all appointments on that date when created

## User Flow

### Doctor Setting Up Availability:

1. Doctor logs in and goes to "Manage Availability"
2. Selects days of the week they work (e.g., Monday, Wednesday, Friday)
3. Sets start and end times for each day
4. Saves the weekly schedule

### Doctor Creating Appointment Slots:

1. Doctor goes to "Manage Slots"
2. Creates specific time slots for upcoming dates
3. Sets how many patients can book each slot
4. Slots appear in patient booking interface

### Doctor Taking a Day Off:

1. Doctor goes to "Manage Days Off"
2. Selects a date and provides a reason
3. System automatically cancels all appointments on that date
4. Patients and admin are notified of cancellations

### Patient Booking Appointment:

1. Patient selects a doctor/service
2. Chooses an appointment date from available dates
3. Selects a time slot from available slots on that date
4. Completes booking with payment (if required)
5. Appointment is created and slot booking count is incremented

## API Endpoints

### Doctor Endpoints:
- `GET/POST /doctor/manage-availability/` - View and update weekly availability
- `GET/POST /doctor/manage-slots/` - View, create, and delete appointment slots
- `POST /doctor/delete-slot/<slot_id>/` - Delete a specific slot
- `GET/POST /doctor/manage-days-off/` - View, create, and delete days off
- `POST /doctor/delete-day-off/<day_off_id>/` - Delete a specific day off

### Patient Endpoints:
- `GET /get-available-slots/` - AJAX endpoint to fetch available slots for a date
- `POST /book-appointment/<service_id>/` - Book appointment with selected slot

## Validation Rules

1. **Slot Creation:**
   - Cannot create slots in the past
   - max_patients must be >= 1
   - end_time must be after start_time

2. **Day Off Creation:**
   - Cannot create days off in the past
   - Automatically cancels all appointments on that date

3. **Appointment Booking:**
   - Can only book available slots
   - Slot must not be fully booked
   - Date must not be a day off
   - Date must match doctor's availability

## Navigation

New menu items added to doctor sidebar:
- Manage Availability
- Manage Slots
- Manage Days Off

## Technical Implementation

- **Framework:** Django
- **Database:** SQLite (via Django ORM)
- **Frontend:** HTML, CSS, JavaScript (AJAX for dynamic slot loading)
- **Authentication:** Django's built-in authentication with custom user model
- **Permissions:** Login required, doctor-only access to management views

## Future Enhancements

Potential improvements:
1. Email notifications when appointments are cancelled
2. SMS reminders for upcoming appointments
3. Bulk slot creation for recurring time slots
4. Calendar view for doctor's schedule
5. Patient waitlist for fully booked slots
6. Appointment rescheduling functionality
7. Doctor can set different slot durations per service
8. Holiday management (auto-create days off for public holidays)

## Files Modified/Created

### Models:
- `doctor/models.py` - Added DoctorAvailability, AppointmentSlot, DayOff models
- `doctor/admin.py` - Registered new models in admin panel

### Views:
- `doctor/views.py` - Added manage_availability, manage_slots, delete_slot, manage_days_off, delete_day_off views
- `base/views.py` - Updated book_appointment and added get_available_slots views

### URLs:
- `doctor/urls.py` - Added routes for new doctor management views
- `base/urls.py` - Added route for get_available_slots

### Templates:
- `templates/doctor/sidebar.html` - Added new menu items
- `templates/doctor/manage_availability.html` - New template
- `templates/doctor/manage_slots.html` - New template
- `templates/doctor/manage_days_off.html` - New template
- `templates/base/book_appointment.html` - Updated to include slot selection

### Migrations:
- `doctor/migrations/0003_appointmentslot_doctoravailability_dayoff.py` - Database migration

## Testing Checklist

- [ ] Doctor can create weekly availability
- [ ] Doctor can create appointment slots
- [ ] Doctor can delete appointment slots
- [ ] Doctor can create days off
- [ ] Days off automatically cancel appointments
- [ ] Patient can see available appointment dates
- [ ] Patient can select time slots
- [ ] Slots become unavailable when fully booked
- [ ] Cannot book appointments on days off
- [ ] Appointments respect doctor's availability
- [ ] Past dates cannot be selected
- [ ] Admin panel shows all new models

## Support

For questions or issues, please contact the development team or refer to the Django documentation.
