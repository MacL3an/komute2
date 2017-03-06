'use strict'; //tells to compiler to not accept 'implicit' variables

class DurationCell extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            duration: ''
        };
    }

    shouldComponentUpdate(nextProps, nextState) {
        if (nextProps.destination !== this.props.destination ||
            nextProps.transitType !== this.props.transitType) {
            this.getDuration(nextProps);
        }
        if (nextState.duration !== this.state.duration) {
            return true;
        }
        return false;
    }

    componentDidMount() {
        this.getDuration(this.props);
    }

    getDuration(nextProps) {
        var url = '/api/duration?origin='+nextProps.origin+'&destination='+nextProps.destination+'&transitType='+nextProps.transitType
        this.serverRequest = $.get(url, function(result) {
            this.setState({
                duration: result.duration
            });
        }.bind(this));
    }

    render() {
        return (
            <td>{this.state.duration}</td>
        );
    }
}

class ListingRow extends React.Component{
    render() {
        var address = this.props.listing.location.address.streetAddress;
        var rooms = this.props.listing.rooms;
        var size = this.props.listing.livingArea;
        var price = this.props.listing.listPrice;
        var origin = this.props.listing.location.position.latitude + "," + this.props.listing.location.position.longitude;
        return (
            <tr>
                <td>{address}</td>
                <td>{rooms}</td>
                <td>{size}</td>
                <td>{price}</td>
                {<DurationCell origin={origin} destination={this.props.destination} transitType={this.props.transitType}/>}
            </tr>
        );
    }
}

class ListingsTable extends React.Component{
    render() {
        var rows = [];
        this.props.listings.forEach((listing) => {
            rows.push(<ListingRow listing={listing} key={listing.booliId}
                destination={this.props.destination}  transitType={this.props.transitType}/>);
        });

        return (
          <table className="table">
            <thead>
              <tr>
                <th>Address</th>
                <th>Rooms</th>
                <th>Size</th>
                <th>Price</th>
                <th>Duration</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>
    );
    }
}

class KomuterApp extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            listings: [],
            destination: '',
            transitType: ''
        };

        this.defaultBooliUrl = 'https://www.booli.se/soderort/914052/?objectType=Parhus%2CRadhus%2CKedjehus&rooms=4';
        this.defaultWorkAddress = 'Sveavägen 44, Stockholm';
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        var apiAddress = "api/listings?";
        var request = apiAddress + this.booliUrl.value;
        this.serverRequest = $.get(request, function(result) {
            this.setState({
                listings: result.listings,
                destination: this.workAddress.value,
                transitType: this.transitType.value
            });
        }.bind(this));
    }

    render() {
        return (
            <div>
                <form>
                    <div>
                        <div className="form-group">
                            <label>Booli URL: </label>
                            <input type="text" className="form-control" defaultValue={this.defaultBooliUrl}  ref={(input) => this.booliUrl = input}/>
                        </div>
                        <div className="form-group">
                            <label>Work address: </label>
                            <input type="text" className="form-control"  defaultValue={this.defaultWorkAddress} ref={(input) => this.workAddress = input}/>
                        </div>
                        <div className="form-group btn-space">
                            <label>Transit type: </label><br/>
                              <select ref={(input) => this.transitType = input}>
                                <option value="transit">Public Transport</option>
                                <option value="bicycle">Bicycle</option>
                                <option value="walking">Walking</option>
                                <option value="driving">Car</option>
                              </select>
                            </div>
                        <div className="form-group">
                            <input className="btn btn-primary btn-space" onClick={this.handleSubmit} type="button" value="Show listings"/>
                        </div>
                    </div>
                </form>
                <h3>Listings:</h3>
                <ListingsTable listings={this.state.listings} destination={this.state.destination} transitType={this.state.transitType}/>
            </div>
        );
    }
}

ReactDOM.render(
    <KomuterApp/>,
    document.getElementById('root')
);