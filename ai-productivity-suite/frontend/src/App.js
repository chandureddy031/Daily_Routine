import React, { useState } from 'react';
import TaskQueue from './components/TaskQueue';
import ApprovalModal from './components/ApprovalModal';
import './App.css';

function App() {
    const [approvalTask, setApprovalTask] = useState(null);

    return (
        <div className="App">
            <header>
                <h1>Unify Dashboard</h1>
            </header>
            <main>
                <TaskQueue />
                {approvalTask && (
                    <ApprovalModal 
                        task={approvalTask}
                        onApprove={id => {
                            console.log("Approved", id);
                            setApprovalTask(null);
                        }}
                        onClose={() => setApprovalTask(null)}
                    />
                )}
            </main>
        </div>
    );
}

export default App;