import React, { useState, useEffect } from 'react';
import { getTasks } from '../services/api';

export default function TaskQueue() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        const loadTasks = async () => {
            const response = await getTasks();
            setTasks(response.documents);
        };
        loadTasks();
    }, []);

    return (
        <div className="task-queue">
            <h2>Task Queue</h2>
            <ul>
                {tasks.map(task => (
                    <li key={task.$id}>
                        <strong>{task.details.type}</strong>
                        <p>{task.email_subject}</p>
                        <p>Status: {task.status}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}