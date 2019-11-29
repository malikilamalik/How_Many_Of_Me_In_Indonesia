import React, { Component , Fragment} from 'react'

import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {getTotalnama} from '../../actions/totalnama';
import totalnama from '../../reducers/totalnama';

export class MainApp extends Component {
    componentDidMount(){
        this.props.getTotalnama(name);
    }
    state ={
        name:""
    }
    onChange = e => this.setState({[e.target.name]:e.target.value});
    onSubmit = e =>{
        e.preventDefault();
        console.log("submit");
        const {name} = this.state;
        const nama = {name};
        console.log(nama);
        this.props.getTotalnama(name);
    }
    render() {
        const {name} = this.state;
        return (
            <Fragment>
                <div className="card card-body mt-4 mb-4">
                    <form onSubmit = {this.onSubmit}>
                        <div className="form-group">
                            <label>Nama</label>
                            <input className="form-control" type="text" name="name" value={name} onChange={this.onChange}>
                            </input>
                        </div>
                        <div className="form-group">
                            <button type="submit" className="btn-primary" value="Submit">Submit</button>
                        </div>
                    </form>
                </div>
                <table className="table table-striped">
                    <thead>
                        <th>
                            Nama
                        </th>
                        <th>
                            Total
                        </th>
                        <th>
                            Laki-Laki
                        </th>
                        <th>
                            Perempuan
                        </th>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{this.props.totalnama.nama}</td>
                            <td>{this.props.totalnama.total}</td>
                            <td>{this.props.totalnama.totalnamalaki}</td>
                            <td>{this.props.totalnama.totalnamaperempuan}</td>
                        </tr>
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    totalnama:state.totalnama.totalnama
});
export default connect(mapStateToProps,{getTotalnama})(MainApp);
