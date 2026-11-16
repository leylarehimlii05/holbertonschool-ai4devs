function updateUserPermissions(userProfile, newPermissions) {
  // Bug 1: Object.assign creates a shallow copy; mutating permissions mutates original object
  const updatedProfile = Object.assign({}, userProfile);
  updatedProfile.permissions.push(...newPermissions);
  return updatedProfile;
}

function findUserById(users, targetId) {
  // Bug 2: Strict equality (===) fails when targetId arrives as a numeric string from URL params
  return users.find((user) => user.id === targetId) || null;
}

module.exports = { updateUserPermissions, findUserById };
