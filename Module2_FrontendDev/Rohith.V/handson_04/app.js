import { courses } from './data.js';

let cachedNotificationsData = [];
let cachedCoursesData = [];

const coursesGrid = document.querySelector('.courses-grid');
const totalCreditsDisplay = document.querySelector('#total-credits');
const promiseLog = document.querySelector('#promise-log');
const notificationsContainer = document.querySelector('#notifications-container');
const searchInput = document.querySelector('#course-search-input');
const clockDisplay = document.querySelector('#live-clock');
const greetingDisplay = document.querySelector('#dynamic-greeting');

function runLiveDashboardClock() {
    const updateTimeStrings = () => {
        const snapshot = new Date();
        clockDisplay.textContent = snapshot.toLocaleTimeString();
        
        const currentHour = snapshot.getHours();
        if (currentHour < 12) {
            greetingDisplay.textContent = " Good Morning, John!";
        } else if (currentHour < 17) {
            greetingDisplay.textContent = "Good Afternoon, John!";
        } else {
            greetingDisplay.textContent = "Good Evening, John!";
        }
    };
    updateTimeStrings();
    setInterval(updateTimeStrings, 1000);
}

const renderNotificationsGrid = (targetData) => {
    notificationsContainer.innerHTML = '';
    
    if (targetData.length === 0) {
        notificationsContainer.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
                <p style="font-weight: 600;">🔍 No matching notifications found</p>
            </div>
        `;
        return;
    }
    
    targetData.forEach((post) => {
        const card = document.createElement('div');
        card.className = 'notification-card';
        card.innerHTML = `
            <h4>📢 ${post.title} (User ID: ${post.userId})</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #475569;">${post.body}</p>
        `;
        notificationsContainer.appendChild(card);
    });
};

const renderCoursesGrid = (filteredCourses = []) => {
    coursesGrid.innerHTML = '';

    if (filteredCourses.length === 0) {
        coursesGrid.innerHTML = `
            <p class="loading-text" style="grid-column: 1 / -1; text-align: center; color: var(--text-secondary);">
                🔍 No courses match your search criteria.
            </p>
        `;
        return;
    }

    filteredCourses.forEach((course) => {
        const card = document.createElement('article');
        card.className = 'course-card';
        card.innerHTML = `
            <span class="course-code">${course.code}</span>
            <h3>${course.name}</h3>
            <p>${course.credits} Credits assigned</p>
        `;
        coursesGrid.appendChild(card);
    });
};

searchInput.addEventListener('input', (event) => {
    const currentQueryText = event.target.value.toLowerCase().trim();
    const courseCards = document.querySelectorAll('.course-card');

    courseCards.forEach((card) => {
        const titleText = card.querySelector('h3').textContent.toLowerCase();
        const codeText = card.querySelector('.course-code').textContent.toLowerCase();

        if (titleText.includes(currentQueryText) || codeText.includes(currentQueryText)) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
});

function fetchUser(id) {
    return fetch('https://jsonplaceholder.typicode.com/users/' + id)
        .then((response) => response.json())
        .then((userData) => {
            console.log(`Traditional Fetch - User Name: ${userData.name}`);
            return userData;
        });
}

async function fetchUserAsync(id) {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users/' + id);
        const userData = await response.json();
        console.log(`Modern Fetch - User Name: ${userData.name}`);
        return userData;
    } catch (error) {
        console.error("Could not fetch user profile details:", error);
    }
}

function fetchAllCourses() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(courses);
        }, 1000);
    });
}

async function loadDashboardLifecycle() {
    coursesGrid.innerHTML = `<p class="loading-text">⏳ Syncing academic course modules...</p>`;

    const liveCoursesArray = await fetchAllCourses();
    cachedCoursesData = liveCoursesArray;
    renderCoursesGrid(cachedCoursesData);

    const totalUnits = cachedCoursesData.reduce((acc, item) => acc + item.credits, 0);
    totalCreditsDisplay.textContent = `Total Enrolled Credits: ${totalUnits} Units`;
}

async function runConcurrentBatchFetches() {
    try {
        const req1 = fetch('https://jsonplaceholder.typicode.com/users/1').then(res => res.json());
        const req2 = fetch('https://jsonplaceholder.typicode.com/users/2').then(res => res.json());

        const [user1Data, user2Data] = await Promise.all([req1, req2]);

        promiseLog.innerHTML = `
            ✅ <strong>Promise.all Completed Successfully:</strong><br>
            👤 User 1 Profile loaded: <strong>${user1Data.name}</strong><br>
            👤 User 2 Profile loaded: <strong>${user2Data.name}</strong>
        `;
    } catch (err) {
        promiseLog.textContent = "Failed batch execution processes.";
    }
}

axios.interceptors.request.use((config) => {
    console.log(`API call started: ${config.url}`);
    return config;
});

async function apiFetch(url, searchParams = {}) {
    const response = await axios.get(url, { 
        params: searchParams,
        timeout: 5000 
    });
    return response.data;
}

async function loadNotificationsPanel(targetUrl, filterParams = {}) {
    try {
        notificationsContainer.innerHTML = `
            <div style="text-align: center; padding: 1rem;">
                <div class="spinner"></div>
                <p style="color: #666; font-style: italic;">Parsing background server bulletins...</p>
            </div>
        `;

        const postsData = await apiFetch(targetUrl, filterParams);
        cachedNotificationsData = postsData.slice(0, 3);
        renderNotificationsGrid(cachedNotificationsData);

    } catch (error) {
        notificationsContainer.innerHTML = `
            <div class="error-alert">
                <div>
                    <strong>⚠️ Connection Error:</strong> 
                    <span>Unable to compile network notifications panel right now. (${error.message})</span>
                </div>
                <button class="retry-btn" id="notifications-retry-trigger">Retry Connection</button>
            </div>
        `;

        document.querySelector('#notifications-retry-trigger').addEventListener('click', () => {
            loadNotificationsPanel('https://jsonplaceholder.typicode.com/posts', { userId: 1 });
        });
    }
}

runLiveDashboardClock();
fetchUser(1);
fetchUserAsync(2);
loadDashboardLifecycle();
runConcurrentBatchFetches();
loadNotificationsPanel('https://jsonplaceholder.typicode.com/nonexistent-broken-route');