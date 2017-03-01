'use strict'; //tells to compiler to not accept 'implicit' variables

var DurationCell = React.createClass({
    getInitialState: function() {
        return {
            duration: ''
        };
    },

    componentDidMount: function() {
        var url = '/api/duration?origin='+this.props.origin+'&destination='+this.props.destination+'&transitType='+this.props.transitType
        console.log(url)
        var that = this;
        this.serverRequest = $.get(url, function(result) {
            that.setState({
                duration: result.duration
            });
        });
    },

    render: function() {
        return (
            <td>{this.state.duration}</td>
        );
    }
});

var ListingRow = React.createClass({
    render: function() {
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
});

var ListingsTable = React.createClass({
    getInitialState: function() {
        return {
            listings: []
        };
    },

    componentDidMount: function() {
        var apiAddress = "api/listings?https://www.booli.se/soderort/914052/?objectType=Parhus%2CRadhus%2CKedjehus&rooms=4";
        this.serverRequest = $.get(apiAddress, function(result) {
            this.setState({
                listings: result.listings
            });
        }.bind(this));
    },

    render: function() {
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
        );}
    });

ReactDOM.render(
    <ListingsTable/>,
    document.getElementById('root')
);