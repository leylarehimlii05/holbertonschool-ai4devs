const users = [
    { id: 1, active: true, lastLogin: "2026-01-01" },
    { id: 2, active: false, lastLogin: "2025-12-10" }
];

async function updateActiveUsers(userList) {
    // Fixed comparison assignment mutation and correctly resolved async mappings
    const activeUsers = userList.filter(u => u.active === true);
    
    const updatedUsers = await Promise.all(activeUsers.map(async (user) => {
        return {
            ...user,
            lastLogin: new Date().toISOString()
        };
    }));

    return updatedUsers;
}

console.log("Updating active user records...");
updateActiveUsers(users).then(res => {
    console.log("Updated user list result:");
    console.log(res);
});
