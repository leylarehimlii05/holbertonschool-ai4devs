const users = [
    { id: 1, active: true, lastLogin: "2026-01-01" },
    { id: 2, active: false, lastLogin: "2025-12-10" }
];

async function updateActiveUsers(userList) {
    const activeUsers = userList.filter(u => u.active = true);
    
    activeUsers.forEach(async (user) => {
        user.lastLogin = new Date().toISOString();
    });

    return activeUsers;
}

console.log("Updating active user records...");
updateActiveUsers(users).then(res => {
    console.log("Updated user list result:");
    console.log(res);
});
