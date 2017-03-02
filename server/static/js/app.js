'use strict'; //tells to compiler to not accept 'implicit' variables

class DurationCell extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            duration: ''
        };
    }

    componentDidMount() {
        var url = '/api/duration?origin='+this.props.origin+'&destination='+this.props.destination+'&transitType='+this.props.transitType
        var that = this;
        this.serverRequest = $.get(url, function(result) {
            that.setState({
                duration: result.duration
            });
        });
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
                {<DurationCell origin={origin} destination="Sveavägen 25, Stockholm" transitType="transit"/>}
            </tr>
        );
    }
}

class ListingsTable extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            listings: []
        };
    }

    componentDidMount() {
        var apiAddress = "api/listings?https://www.booli.se/soderort/914052/?objectType=Parhus%2CRadhus%2CKedjehus&rooms=4";
        this.serverRequest = $.get(apiAddress, function(result) {
            this.setState({
                listings: result.listings
            });
        }.bind(this));
    }

    render() {
            var rows = [];
            this.state.listings.forEach(function(listing) {
                rows.push(<ListingRow listing={listing} key={listing.booliId} />);
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
    render() {
        return (
            <div>
                <form>
                    <div>
                        <div className="form-group">
                            <label>Booli URL: </label>
                            <input id="booliUrl" className="form-control" type="text"/>
                        </div>
                        <div className="form-group">
                            <label>Work address: </label>
                            <input type="text" className="form-control"/>
                        </div>
                        <div className="form-group btn-space">
                            <label>Transit type: </label><br/>
                            <select>
                            </select>
                            </div>
                        <div className="form-group">
                            <input className="btn btn-primary btn-space" type="button" value="Show listings"/>
                        </div>
                    </div>
                </form>
                <h3>Listings:</h3>
                <ListingsTable/>
            </div>
        );
    }
}

ReactDOM.render(
    <KomuterApp/>,
    document.getElementById('root')
);