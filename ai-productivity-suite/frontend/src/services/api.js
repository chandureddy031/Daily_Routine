import { Client, Databases } from 'appwrite';

const client = new Client()
    .setEndpoint(process.env.REACT_APP_APPWRITE_ENDPOINT)
    .setProject(process.env.REACT_APP_APPWRITE_PROJECT_ID);

const databases = new Databases(client);

export const getTasks = async () => {
    return await databases.listDocuments('unify', 'tasks');
};

export const updateTask = async (taskId, data) => {
    return await databases.updateDocument('unify', 'tasks', taskId, data);
};