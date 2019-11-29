import React,{ Fragment } from 'react';
import Form from './Form';
import MainApp from './MainApp';

export default function Dashboard() {
    return (
        <div>
            <Fragment>
                <Form/>
                <MainApp/>
            </Fragment>
        </div>
    )
}
