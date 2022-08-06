import React from 'react'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import { blue } from '@mui/material/colors';

function ProductCard({ card_height, img_url, name, alt }) {
    return (
        <Card >
            <CardActionArea>
                <CardMedia
                    component="img"
                    height={card_height}
                    image={img_url}
                    alt={alt}
                />
                <CardContent style={{ backgroundColor: blue[200] }}>
                    <Typography gutterBottom variant="h7" component="div">
                        {name}
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>


    )
}

export default ProductCard