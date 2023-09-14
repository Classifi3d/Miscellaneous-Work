package com.project.TheGallery.service;

import com.project.TheGallery.entity.Artist;
import com.project.TheGallery.repository.ArtistRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Random;
@Service
public class GalleryServiceImplementation implements GalleryService{
    @Autowired
    private ArtistRepository artistRepository;

    @Override
    public List<Artist> fetchArtistList(){
        return artistRepository.findAll();
    }

    @Override
    public Artist fetchArtistId(Integer artistId){
        //add NoFoundException
        return artistRepository.findById(artistId).get();
    }
    @Override
    public Artist fetchArtistRandom(){

        return artistRepository.findArtistRandom();
    }
    @Override
    public List<Artist> fetchArtistRandomList(Integer artistCount){

        return artistRepository.findArtistRandomList(artistCount);
    }

    public List<Artist> fetchArtistRandom10(){

        return artistRepository.findArtistRandom10();
    }

    public Artist fetchArtistByName(String artistName){
        return artistRepository.findArtistByName(artistName);
    }


//    public Artist fetchArtistPicureById(String artistName,Integer pictureId){
//        return  artistRepository.findArtistPictureById(artistName,pictureId);
//    }

}
