import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import { Grid } from '@mui/material';
import React, { useEffect, useState } from 'react';
import ProductCard from '../products/ProductCard';
import Checkout from '../common/Checkout';

function fetchCategories() {
    const [data, setData] = useState([[]]);
    const request_options = {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    };
    const getData = () => {
        fetch("/api/fetch-category", request_options)
            .then((response) => response.json())
            .then((myJson) => setData(myJson));
    }
    useEffect(() => {
        getData();
    }, []);

    return data;
}

function fetchProductDrinks() {
    const [data, setData] = useState([[]]);
    const request_options = {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    };
    const getData = () => {
        fetch("/api/fetch-product-drinks", request_options)
            .then((response) => response.json())
            .then((myJson) => setData(myJson));
    }
    useEffect(() => {
        getData();
    }, []);

    return data;
}

function fetchProductBreakfast() {
    return;
}

function fetchProductAsianFood() {
    return;
}

function fetchProductKid() {
    return;
}

function fetchProductSnack() {
    return;
}

function fetchProductDessert() {
    return;
}

// function FetchOptionDrinks() {
//     const [data, setData] = useState([[]]);
//     const request_options = {
//         method: "GET",
//         headers: { "Content-Type": "application/json" },
//     };
//     const getData = () => {
//         fetch("/api/fetch-option", request_options)
//             .then((response) => response.json())
//             .then((myJson) => setData(myJson));
//     }
//     useEffect(() => {
//         getData();
//     }, []);

//     return data;
// }

function createPannel(categorie_data) {
    if (typeof categorie_data != "undefined") {
        return (<Box sx={{ flexGrow: 1, padding: 2 }}>
            <Grid container spacing={2}>
                {/* Get value from database */}
                {
                    categorie_data.map((product) => (
                        <Grid item xs={2.4}>
                            <ProductCard
                                img_url={product.image}
                                card_height={60}
                                name={product.name}
                                alt={product.name}
                            />
                        </Grid>)
                    )}
            </Grid>
        </Box>);
    }

    return;
}
function TabPanel(props) {
    const { children, value, index, ...other } = props;
    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`vertical-tabpanel-${index}`}
            aria-labelledby={`vertical-tab-${index}`}
            {...other}
            sx={{ display: "flex" }}
        >
            {value === 0 && (createPannel(fetchProductDrinks()))}
            {value === 1 && (createPannel(fetchProductBreakfast()))}
            {value === 2 && (createPannel(fetchProductAsianFood()))}
            {value === 3 && (createPannel(fetchProductKid()))}
            {value === 4 && (createPannel(fetchProductSnack()))}
            {value === 5 && (createPannel(fetchProductDessert()))}
        </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
};

function a11yProps(index) {
    return {
        key: index,
        id: `vertical-tab-${index}`,
        'aria-controls': `vertical-tabpanel-${index}`,
    };
}

function makeProducts(selectedTab) {
    // SQL data base
    return (
        <>
            {/* TODO Flex 5 items */}
            <TabPanel value={selectedTab} index={0} ></TabPanel>
            <TabPanel value={selectedTab} index={1} ></TabPanel>
        </>
    );
}

function TabPanelHandler(selectedTab, contents) {
    var content;
    if (selectedTab !== undefined) {
        content = makeProducts(selectedTab);
    }

    return (
        <>
            {content}
        </>
    );
}

function VerticalTabs(categories) {
    const [selectedTab, setSelectedTab] = useState(0);

    const handleChange = (event, newValue) => {
        setSelectedTab(newValue);
    };

    return (
        <>
            <Box sx={{ position: 'fixed', bgcolor: 'background.paper', left: 0, marginTop: 8, bottom: 0, width: 125, top: 0 }}>
                <Tabs
                    orientation="vertical"
                    variant="standard"
                    value={selectedTab}
                    onChange={handleChange}
                    aria-label="Vertical Catigoury"
                    sx={{ borderRight: 1, borderColor: 'divider', height: '100%' }}
                >
                    {
                        categories.map((category) => (<Tab label={category.name} {...a11yProps(category.id - 1)} sx={{ height: 125, fontWeight: "bold" }} />))
                    }
                </Tabs>
            </ Box>
            <Box sx={{ display: 'flex', marginTop: 8, marginLeft: 15.5, height: '100%' }}>
                <Box sx={{ flex: 3 }}>
                    {TabPanelHandler(selectedTab)}
                </Box>
                <Box sx={{ flex: 1 }}>
                    <Checkout />
                </Box>
            </Box>
        </>
    );
}

function VerticalTabPanel() {
    const categories = fetchCategories();
    console.log(categories);
    return (
        VerticalTabs(categories)
    )
}

export default VerticalTabPanel