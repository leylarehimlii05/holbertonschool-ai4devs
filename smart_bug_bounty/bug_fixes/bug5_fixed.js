function updateUserPermissions(userProfile, newPermissions) {
  return {
    ...userProfile,
    permissions: [...(userProfile.permissions || []), ...newPermissions],
  };
}

function findUserById(users, targetId) {
  if (targetId === null || targetId === undefined) {
    return null;
  }
  return users.find((user) => String(user.id) === String(targetId)) || null;
}

module.exports = { updateUserPermissions, findUserById };
