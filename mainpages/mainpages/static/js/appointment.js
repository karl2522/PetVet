// Calendar functionality
function generateCalendar() {
    const today = new Date();
    const currentMonth = today.getMonth();
    const currentYear = today.getFullYear();
    
    const firstDay = new Date(currentYear, currentMonth, 1);
    const lastDay = new Date(currentYear, currentMonth + 1, 0);
    
    const calendarDays = document.getElementById('calendar-days');
    calendarDays.innerHTML = '';
    
    // Add empty cells for days before the first day of the month
    for (let i = 0; i < firstDay.getDay(); i++) {
        calendarDays.innerHTML += '<div></div>';
    }
    
    // Add days of the month
    for (let day = 1; day <= lastDay.getDate(); day++) {
        const dayElement = document.createElement('div');
        dayElement.textContent = day;
        
        // Add marker for specific dates (example)
        if ([4, 7, 15, 17, 31].includes(day)) {
            dayElement.classList.add('has-appointment');
        }
        
        // Highlight current day (example)
        if (day === 20) {
            dayElement.classList.add('current-day');
        }
        
        calendarDays.appendChild(dayElement);
    }
}

// Generate appointments
function generateAppointments() {
    const appointments = [
        { doctor: "Dr. Jared Omen", pet: "Oreo", reason: "1st Vaccine", date: "19 Oct", time: "1:00 PM", status: "Confirmed" },
        { doctor: "Dr. Jared Omen", pet: "Oreo", reason: "1st Vaccine", date: "19 Oct", time: "1:00 PM", status: "Cancelled" },
        { doctor: "Dr. Jared Omen", pet: "Oreo", reason: "1st Vaccine", date: "19 Oct", time: "1:00 PM", status: "Confirmed" },
        { doctor: "Dr. Jared Omen", pet: "Oreo", reason: "1st Vaccine", date: "19 Oct", time: "1:00 PM", status: "Cancelled" }
    ];

    const appointmentsContainer = document.querySelector('.appointments');
    appointments.forEach(apt => {
        appointmentsContainer.innerHTML += `
            <div class="appointment-item">
                <div class="doctor">
                    <div class="avatar"></div>
                    <span>${apt.doctor}</span>
                </div>
                <div>${apt.pet}</div>
                <div>${apt.reason}</div>
                <div>${apt.date}</div>
                <div>${apt.time}</div>
                <div class="status ${apt.status.toLowerCase()}">${apt.status}</div>
            </div>
        `;
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    generateCalendar();
    generateAppointments();
});