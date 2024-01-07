document.addEventListener('DOMContentLoaded', function() {
    const events = [
        { date: '2024-01-01', content: 'New Year\'s Day' },
        { date: '2024-02-14', content: 'Valentine\'s Day' },
        { date: '2024-07-04', content: 'Independence Day' },
        { date: '2024-12-25', content: 'Christmas Day' }
    ];

    const timeline = document.getElementById('timeline');

    events.forEach(event => {
        const div = document.createElement('div');
        div.className = 'timeline-event';
        div.innerHTML = `<strong>${event.date}</strong>: ${event.content}`;
        timeline.appendChild(div);
    });
});
